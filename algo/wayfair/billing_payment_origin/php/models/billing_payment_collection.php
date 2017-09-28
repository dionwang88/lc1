<?php
/**
 * The Billing Payment Collection
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */
namespace WF\Shared\Models\Overpack;

use WF\Shared\DAOs\Overpack\Billing_Payment_DAO;
use WF\Shared\View_Classes\Fulfillment\billing_payment\Overpack_Carrier_Data;

class Billing_Payment_Collection extends \WF\Shared\Models\Base_Collection {

  /**
   * @var string the field of from_date
   */
  public $from_date;
  /**
   * @var string the field of to_date
   */
  public $to_date;
  /**
   * @var string the field of filter_by
   */
  public $filter_by;
  /**
   * @var string the field of sort_by
   */
  public $sort_by;
  /**
   * @var string the field of user_name
   */
  public $user_name;
  /**
   * @var string the field of admin
   */
  public $admin;
  /**
   * @var string the field of keyword
   */
  public $keyword;
  /**
   * @var int the field of carrier id
   */
  public $ts_id;
  /**
   * @var \WF\Shared\DAOs\Overpack\Billing_Payment_DAO
   */
  protected $dao;

  /**
   * Billing_Payment_Collection constructor.
   *
   * @param \WF\Shared\DAOs\Base_DAO $dao Dao to use for this model
   */
  public function __construct($dao = null) {
    parent::__construct($dao ?: new Billing_Payment_DAO());
  }

  /**
   * creates, populates, and returns a model object from the given array.
   *
   * @param array $map an associative array that can be used to populate whichever type of model a subclass needs.
   *
   * @return \WF\Shared\Models\Overpack\Billing_Payment_Collection objects populated from the given map.
   */
  public function create_model($map) {

    $billing_payment_model = new Billing_Payment_Model();
    $billing_payment_model->populate($map);
    return $billing_payment_model;
  }

  /**
   * Loads billing and payment list from DB
   * @param string $from_date from date
   * @param string $to_date   to date
   * @param int    $carrier   carrier id
   * @param string $keyword   keyword
   * @param string $user_name user name
   * @param int    $admin     admin id
   * @param string $filter_by filter by field
   * @param string $sort_by   sort by field
   * @return null
   */
  public function load_billing_payment($from_date, $to_date, $carrier, $keyword, $user_name, $admin, $filter_by, $sort_by) {
    $results = $this->dao->get_billing_payment($from_date, $to_date, $carrier, $keyword, $user_name, $admin, $filter_by, $sort_by);
    $this->populate($results);
  }

  /**
   * Get overpack carrier list
   *
   * @return array|mixed the result list of overpack carriers array
   */
  public function get_overpack_carrier_list() {
    $results = $this->dao->get_overpack_carrier_list();
    $overpack_carriers = [];
    foreach ($results as $map) {
      $oc = new Overpack_Carrier_Data();
      $oc->overpack_carrier = ['carrier_id' => $map['TsID'], 'carrier_name' => $map['TsName']];
      $overpack_carriers[] = $oc;
    }
    return $overpack_carriers;
  }

  /**
   * Update the status for the selected billing and payment rows
   * @param array $slm_ids the array of slm_id
   * @param array $saa_ids the array of saa_id
   * @return null
   */
  public function update_status_to_approved($slm_ids, $saa_ids) {
    $this->dao->update_status_to_approved($slm_ids, $saa_ids);
  }
}