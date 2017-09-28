<?php
/**
 * The Billing Payment DAO
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */

namespace WF\Shared\DAOs\Overpack;

use WF\Shared\Logging\Logger;
use WF\Shared\PDO;

class Billing_Payment_DAO extends \WF\Shared\DAOs\Base_DAO {
  /**
   * The Logger instance
   *
   * @var \WF\Shared\Logging\Logger
   */
  private $logger;

  /**
   * Get the Logger instance
   *
   * @return \WF\Shared\Logging\Logger the Logger instance
   */
  private function get_logger() {
    if (!isset($this->logger)) {
      $this->logger = Logger::use_logger('Delivery_Route_DAO');
    }
    return $this->logger;
  }

  /**
   * Get billing and payment records from store procedure
   *
   * @param string $from_date from date
   * @param string $to_date   to date
   * @param int    $ts_id     carrier id
   * @param string $keyword   keyword
   * @param int    $user_name user name
   * @param string $admin     admin id
   * @param string $filter_by filtered by field
   * @param string $sort_by   sorted by field
   *
   * @return array|mixed    list of billing and payments
   */
  public function get_billing_payment($from_date, $to_date, $ts_id, $keyword, $user_name, $admin, $filter_by, $sort_by) {
    $sql = 'exec spGetExtranetLoadPaymentData
    @from_date  = :from_date,
    @to_date    = :to_date,
    @filter_by  = :filter_by,
    @sort_by    = :sort_by,
    @user_name  = :user_name,
    @admin      = :admin,
    @keyword    = :keyword,
    @ts_id      = :ts_id';

    $statement = PDO::new_statement('OT', $sql);

    $statement->bindValue(':from_date', $from_date, PDO::PARAM_STR);
    $statement->bindValue(':to_date', $to_date, PDO::PARAM_STR);
    $statement->bindValue(':filter_by', $filter_by, PDO::PARAM_STR);
    $statement->bindValue(':sort_by', $sort_by, PDO::PARAM_STR);
    $statement->bindValue(':user_name', $user_name, PDO::PARAM_STR);
    $statement->bindValue(':admin', $admin, PDO::PARAM_INT);
    $statement->bindValue(':keyword', $keyword, PDO::PARAM_STR);
    $statement->bindValue(':ts_id', $ts_id, PDO::PARAM_INT);

    return $statement->execute() ? $statement->fetchAll() : [];
  }

  /**
   * Get overpack carrier list
   *
   * @return array|mixed
   */
  public function get_overpack_carrier_list() {
    $sql = '
      SELECT TsID, TsName + \' (\' + cast(TsID as varchar) + \')\' as TsName
      FROM tblThirdPartyCarrier with(nolock)
      WHERE TsName is not null and TsOverpackProvider = 1
      ORDER BY TsName';

    $statement = PDO::new_statement('OT', $sql);
    return $statement->execute() ? $statement->fetchAll() : [];
  }

  /**
   * get list of PO's for given OPlCarrierRefID for billing Screen
   * @param  int $saa_id saa id
   * @param  int $slm_id slm id
   * @return array|mixed billing array
   */
  public function get_extranet_payment_by_po($saa_id, $slm_id) {
    $sql = 'exec spGetExtranetPaymentDataByPO
        @saa_id     = :saa_id,
        @slm_id     = :slm_id';

    $statement = PDO::new_statement('OT', $sql);
    $statement->bindValue(':saa_id', $saa_id, PDO::PARAM_INT);
    $statement->bindValue(':slm_id', $slm_id, PDO::PARAM_INT);

    return $statement->execute() ? $statement->fetchAll() : [];
  }

  /**
   * get list of OP's for given OPlCarrierRefID and PO Num for billing Screen
   *
   * @param int $saa_id saa id
   * @param int $slm_id slm id
   * @param int $opl_id opl id
   *
   * @return array|mixed billing payment item array
   */
  public function get_extranet_payment_by_item($saa_id, $slm_id, $opl_id) {

    $sql = 'exec spGetExtranetPaymentDataByItem
        @saa_id     = :saa_id,
        @slm_id     = :slm_id,
        @opl_id     = :opl_id';

    $statement = PDO::new_statement('OT', $sql);
    $statement->bindValue(':saa_id', $saa_id, PDO::PARAM_INT);
    $statement->bindValue(':slm_id', $slm_id, PDO::PARAM_INT);
    $statement->bindValue(':opl_id', $opl_id, PDO::PARAM_INT);

    return $statement->execute() ? $statement->fetchAll() : [];
  }


  /**
   * Update Carton Information
   *
   * @param string $opi_id           opi_id                    overpack load item id
   * @param string $opl_id           opl_id                    overpack load id
   * @param string $carton_count     opi_corrected_cartonCount overpack load item corrected carton count
   * @param string $weight           opi_corrected_weight      overpack load item corrected weight
   * @param string $leg_type         leg_type                  type of leg
   * @param int    $ask_for_approval opi_approved              the status of approved
   *
   * @return int  estimated cost for final Slm ID
   */
  public function update_carton($opi_id, $opl_id, $carton_count, $weight, $leg_type, $ask_for_approval) {
    $pdo = PDO::new_instance('OT');
    $net_pay = 0;
    try {
      $pdo->beginTransaction();
      $update_opi = ' UPDATE tblOverpackItem
                      SET    OpiCorrectedWeight= :opi_corrected_weight,
                             OpiCorrectedCartonCount= :opi_corrected_cartonCount,
                             OpiApproved= :opi_approved
                      WHERE  OpiID= :opi_id;
                      EXEC   spUpdateOverpackInfo @OplID = :opl_id;';

      $statement = $pdo->prepare($update_opi);
      $statement->bindValue(':opi_corrected_weight', $weight, PDO::PARAM_INT);
      $statement->bindValue(':opi_corrected_cartonCount', $carton_count, PDO::PARAM_INT);
      $statement->bindValue(':opi_approved', $ask_for_approval, PDO::PARAM_INT);
      $statement->bindValue(':opi_id', $opi_id, PDO::PARAM_INT);
      $statement->bindValue(':opl_id', $opl_id, PDO::PARAM_INT);

      if (!$statement->execute()) {
        $error = 'Failed to save to tblTransInternProduct';
        return ['errors' => $error];
      }

      //ping tms and save estimated cost for final Slm ID
      $slm_sql = '
                SELECT OplSlmID, OplSlmOutID
                FROM   tblOverpackItem WITH(nolock)
                INNER JOIN tblOverpackLoad WITH (nolock) ON OpiOlId = OplID
                WHERE  OpiID= :opi_id;';

      $statement = $pdo->prepare($slm_sql);
      $statement->bindValue(':opi_id', $opi_id, PDO::PARAM_INT);
      $slm_rs = $statement->execute() ? $statement->fetchAll() : [];

      if (!empty($slm_rs[0]['OplSlmID'])) {
        $billing_source = 'OVERPACK_INBOUND';
        if (strtolower($leg_type) == 'delivery') {
          $final_slm_id = $slm_rs[0]['OplSlmOutID'];
          $billing_source = 'OVERPACK_OUTBOUND';
        } else {
          $final_slm_id = $slm_rs[0]['OplSlmID'];
        }
        //ping tms and save estimated cost for final Slm ID
        $net_pay = retrieve_net_pay_per_manifest($final_slm_id, 7);
        update_sli_weights_and_class($final_slm_id, $billing_source);

        if ($ask_for_approval == 2) {
          //put slm status in review
          $update_sql = ' UPDATE tblShippingLoadManifest
                          SET    SlmInvoiceStatus = 3
                          WHERE  SlmInvoiceStatus <> 3
                          AND    SlmID = :final_slm_id;';

          $statement = $pdo->prepare($update_sql);
          $statement->bindValue(':final_slm_id', $final_slm_id, PDO::PARAM_INT);
          if (!$statement->execute()) {
            $error = 'Failed to save to tblTransInternProduct';
            return ['errors' => $error];
          }
        }
      }
      $pdo->commit();
    } catch (\Exception $exe) {
      $pdo->rollBack();
    }
    return $net_pay;
  }

  /**
   * Update the status for the selected billing and payment rows
   *
   * @param array $slm_ids the list of slm_id
   * @param array $saa_ids the list of saa_id
   *
   * @return array
   */
  public function update_status_to_approved($slm_ids, $saa_ids) {
    $pdo = PDO::new_instance('OT');
    $update_sql = '';
    try {
      $pdo->beginTransaction();
      if (!empty($slm_ids)) {
        $params = '';
        foreach ($slm_ids as $i => $slm_id) {
          $params .= ':slm_id' . $i . ',';
        }
        $params = substr($params, 0, -1);
        $update_sql = 'UPDATE tblShippingLoadManifest
                       SET SlmInvoiceStatus = 2
                       WHERE SlmID IN ('.$params.') AND SlmInvoiceStatus = 0; ';
      }
      if (!empty($saa_ids)) {
        $params = '';
        foreach ($saa_ids as $i => $saa_id) {
          $params .= ':saa_id' . $i . ',';
        }
        $params = substr($params, 0, -1);
        $update_sql .= 'UPDATE tblServiceAgentAttempt
                      SET SaaInvoiceStatus = 2,
                          SaaInvoiceDate = getdate()
                      WHERE SaaID IN ('.$params.') AND SaaInvoiceStatus = 0;';
      }

      if (!empty($update_sql)) {
        $statement = PDO::new_statement('OT', $update_sql);
        if (!empty($slm_ids)) {
          foreach ($slm_ids as $i => $slm_id) {
            $statement->bindValue(':slm_id' . $i, $slm_id, PDO::PARAM_INT);
          }
        }
        if (!empty($saa_ids)) {
          foreach ($saa_ids as $i => $saa_id) {
            $statement->bindValue(':saa_id', $saa_id, PDO::PARAM_INT);
          }
        }
        if (!$statement->execute()) {
          $error = 'Failed to save to tblTransInternProduct';
          return ['errors' => $error];
        }
        $pdo->commit();

        if (!empty($slm_ids)) {
          foreach ($slm_ids as $slm_id) {
            $slm_log_message = 'Approving invoice for ' . $slm_id;
            log_slm_action($slm_log_message, SLM_INVOICE_STATUS_UPDATE, $slm_id);
          }
        }
      }
    }catch (\Exception $exe) {
      $pdo->rollBack();
    }
  }

  /**
   * Get the accessorial costs for a billing and payment record
   *
   * @param  int $slm_id slm id
   * @param  int $saa_id saa id
   * @return array
   */
  public function get_billing_accessorials($slm_id, $saa_id) {

    $sql = '
        SELECT DISTINCT SvfID, SvfPrice, SvfSvaID, SvfSvacCode, COALESCE(SvfRequestedQty, SvfQty, 0) AS RequestedQty,
        COALESCE(SvfRequestedPrice, SvfPrice, 0) AS RequestedPrice,
        ISNULL(SvfApprovedQty, (CASE WHEN SvfApproved=1 THEN SvfQty ELSE 0 END)) AS ApprovedQty,
        ISNULL(SvfApprovedPrice, (CASE WHEN SvfApproved=1 THEN SvfPrice ELSE 0 END)) AS ApprovedPrice,
        CASE WHEN SvfApproved = 1 THEN \'Yes\' ELSE \'No\' END AS SvfApproved,
        ISNULL(SvfNote,\'-\') AS SvfNote, ISNULL(SvfCodeDesc, SvfSvacCode) AS SvfCodeDesc, SvfChgTypeDesc,
        TsID, TsCuyID
        FROM tblServiceAgentFee WITH(NOLOCK)';
    if ($slm_id > 0) {
      // Joins mapping Ts to Svf through SvfSlmID/SlmTsID, plus the where clause
      $sql .= '
          LEFT JOIN tblShippingLoadManifest WITH(NOLOCK) ON SlmID = SvfSlmID
          LEFT JOIN tblThirdPartyCarrier WITH(NOLOCK) ON TsID = SlmTsID
          WHERE SvfSlmID = :slm_id';
      $statement = PDO::new_statement('OT', $sql);
      $statement->bindValue(':slm_id', $slm_id, PDO::PARAM_INT);
    } else {
      // Joins mapping Ts to Svf through SvfSaaID/SaaSvaID/SvaTsID, plus the where clause
      $sql .= '
          LEFT JOIN tblServiceAgentAttempt WITH(NOLOCK) ON SaaID = SvfSaaID
          LEFT JOIN tblplServiceAgent WITH(NOLOCK) ON SvaID = SaaSvaID
          LEFT JOIN tblThirdPartyCarrier WITH(NOLOCK) ON TsID = SvaTsID
          WHERE SvfSaaID = :saa_id';
      $statement = PDO::new_statement('OT', $sql);
      $statement->bindValue(':saa_id', $saa_id, PDO::PARAM_INT);
    }
    return $statement->execute() ? $statement->fetchAll() : [];
  }
}