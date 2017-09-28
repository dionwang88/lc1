<?php
/**
 * The Extranet Billing Payment Item Model
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */
namespace WF\Shared\Models\Overpack;

use WF\Shared\DAOs\Overpack\Billing_Payment_DAO;

class Billing_Payment_Item_Model extends \WF\Shared\Models\Base_Model {

  /**
   * @var string load id
   */
  public $load_id;

  /**
   * @var int Identifier for the service agent attempt
   */
  public $saa_id;

  /**
   * @var int Overpack load ID
   */
  public $opl_id;

  /**
   * @var int Overpack load purchase order number including the store prefix
   */
  public $opl_po_num_send;

  /**
   * @var int Overpack load carrier reference number
   */
  public $opl_carrier_ref_number;

  /**
   * @var int Overpack load item ID
   */
  public $opi_id;

  /**
   * @var int Overpack load item order product ID
   */
  public $opi_op_id;

  /**
   * @var int Overpack load item quantity
   */
  public $opi_qty;

  /**
   * @var int Overpack load item carton count
   */
  public $opi_carton_count;

  /**
   * @var float Overpack load item corrected weight (OpiWeight * OpiQty)
   */
  public $opi_corrected_weight;

  /**
   * @var int Overpack load pallet weight
   */
  public $opl_pallet_weight;

  /**
   * @var string Overpack load received date
   */
  public $opl_received_date;

  /**
   * @var int Overpack load item corrected carton count
   */
  public $opi_corrected_carton_count;

  /**
   * @var int Overpack load item type ID
   */
  public $opi_overpack_type_id;

  /**
   * @var float Overpack load item cost
   */
  public $opi_overpack_cost;

  /**
   * @var string Order product detail product name
   */
  public $od_pr_name;

  /**
   * @var string Nanufacturer part number
   */
  public $pr_manu_part_num;

  /**
   * @var string Product SKU
   */
  public $pr_sku;

  /**
   * @var string The name of the option
   */
  public $opt_name;

  /**
   * @var string The type of leg
   */
  public $leg_type;

  /**
   * @var int Third party carrier ID
   */
  public $ts_id;

  /**
   * @var string Currency ID
   */
  public $ts_cuy_id;

  /**
   * @var string Load status
   */
  public $load_status;

  /**
   * The DAO
   *
   * @var \WF\Shared\DAOs\Overpack\Billing_Payment_DAO
   */
  protected $dao;

  /**
   * The constructor of Billing_Payment_Item_Model
   * @param null $dao \WF\Shared\DAOs\Overpack\Billing_Payment_DAO
   */
  public function __construct($dao = null) {
    parent::__construct($dao ?: new Billing_Payment_DAO());
  }

  /**
   * Update Carton Information for a billing and payment item
   *
   * @param  int    $opi_id           overpack load item id
   * @param  int    $opl_id           overpack load id
   * @param  int    $opi_carton_count overpack load item carton count
   * @param  int    $opi_weight       overpack load item weight
   * @param  string $leg_type         leg type
   * @param  int    $opi_approved     overpack load item apprived
   * @return int    net_pay net pay
   */
  public function update_carton_count($opi_id, $opl_id, $opi_carton_count, $opi_weight, $leg_type, $opi_approved = 0) {
    return $this->dao->update_carton($opi_id, $opl_id, $opi_carton_count, $opi_weight, $leg_type, $opi_approved);
  }

  /**
   * Populate this model from a map
   *
   * @param array $map the map
   *
   * @return \WF\Shared\Models\Overpack\Billing_Payment_Item_Model|bool the populated model or false if there was an error
   */
  public function populate($map) {
    if (empty($map)) {
      return false;
    }
    parent::populate($map);

    $this->saa_id = $map['SaaID'];
    $this->opl_id = $map['OplID'];
    $this->opl_po_num_send = $map['OplPoNumSend'];
    $this->opl_po_num = $map['OplPoNum'];
    $this->opl_carrier_ref_number = $map['OplCarrierRefNumber'];
    $this->opi_id = $map['OpiID'];
    $this->opi_op_id = $map['OpiOpID'];
    $this->opi_qty = $map['OpiQty'];
    $this->opi_carton_count = $map['OpiCartonCount'];
    $this->opi_corrected_weight = $map['OpiCorrectedWeight'];
    $this->opl_pallet_weight = $map['OplPalletWeight'];
    $this->opl_received_date = $map['OplReceivedDate'];
    $this->opi_corrected_carton_count = $map['OpiCorrectedCartonCount'];
    $this->opi_overpack_type_id = $map['OpiOverpackTypeID'];
    $this->opi_overpack_cost = $map['OpiOverpackCost'];
    $this->od_pr_name = $map['OdPrName'];
    $this->pr_manu_part_num = $map['PrManuPartNum'];
    $this->pr_sku = $map['PrSKU'];
    $this->opt_name = $map['OptName'];
    $this->ts_id = $map['TsID'];
    $this->ts_cuy_id = $map['TsCuyID'];

    return $this;
  }

}
