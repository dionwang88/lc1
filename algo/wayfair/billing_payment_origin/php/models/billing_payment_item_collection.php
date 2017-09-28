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

class Billing_Payment_Item_Collection extends \WF\Shared\Models\Base_Collection {
  /**
   * @var \WF\Shared\DAOs\Overpack\Billing_Payment_DAO
   */
  protected $dao;

  /**
   * Billing_Payment_Item_Collection constructor.
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
   * @return \WF\Shared\Models\Overpack\Billing_Payment_Item_Collection objects populated from the given map.
   */
  public function create_model($map) {

    $billing_payment_item_model = new Billing_Payment_Item_Model();
    $billing_payment_item_model->populate($map);
    return $billing_payment_item_model;
  }

  /**
   * billing payment item reuslts from DB
   *
   * @param  int $saa_id saa id
   * @param  int $slm_id slm id
   * @param  int $opl_id overpack load id
   * @return object Billing Payment Item Collection
   */
  public function load_billing_payment_item($saa_id, $slm_id, $opl_id) {
    $results = $this->dao->get_extranet_payment_by_item($saa_id, $slm_id, $opl_id);
    $this->populate($results);

    return $this;
  }

  /**
   * @return array billing payment item models
   */
  public function get() {
    return $this->models;
  }
}