<?php
/**
 * The Billing Payment Extranet Collection
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */

namespace WF\Shared\Models\Overpack;

use WF\Shared\DAOs\Overpack\Billing_Payment_DAO;

require_once INCLUDE_PATH . '/includes/classes/finance/prorate/prorate_class.php';

class Billing_Payment_Extranet_Collection extends \WF\Shared\Models\Base_Collection {
  /**
   * @var \WF\Shared\DAOs\Overpack\Billing_Payment_DAO
   */
  protected $dao;

  /**
   * @var float Temp variable for compute model cost
   */
  public $use_costs;
  /**
   * @var float Temp variable for compute model cost
   */
  public $use_acc_costs;
  /**
   * @var float Temp variable for compute model cost
   */
  public $prorated_costs;
  /**
   * @var float Temp variable for compute model cost
   */
  public $prorated_acc_costs;

  /**
   * Billing_Payment_Extranet_Collection constructor.
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
   * @return \WF\Shared\Models\Overpack\Billing_Payment_Extranet_Collection objects populated from the given map.
   */
  public function create_model($map) {

    $billing_payment_extranet_model = new Billing_Payment_Extranet_Model();
    $billing_payment_extranet_model->populate($map);
    return $billing_payment_extranet_model;
  }

  /**
   * Get the billing payment extranet list
   *
   * @param  int $saa_id saa id
   * @param  int $slm_id slm id
   * @return object WF\Shared\Models\Overpack\Billing_Payment_Extranet_Collection
   */
  public function load_billing_payment_extranet($saa_id, $slm_id) {
    $results = $this->dao->get_extranet_payment_by_po($saa_id, $slm_id);
    $this->compute_prorate_cost($results);
    $this->populate($results);

    return $this;
  }

  /**
   * Compute the temporary variable for model computing costs
   * @param array $rs results from DAO
   * @return null
   */
  public function compute_prorate_cost($rs) {
    // Build up an array of weights to prorate against
    $weights = array();
    $this->prorated_costs = -1;
    $this->prorated_acc_costs = -1;
    $load_cost = $rs[0]['load_cost'];
    $accessorial_cost = $rs[0]['accessorial_cost'];
    if (!empty($load_cost) || !empty($accessorial_cost)) {
      foreach ($rs as $row) {
        $weights[$row['OplPoNum']] = $row['OplTotalWeight'] + $row['OplPalletWeight'];
      }

      $prorater = new \Prorate();

      if (!empty($load_cost)) {
        $this->prorated_costs = $prorater->prorateValue($load_cost, $weights, 2);
      }

      if (!empty($accessorial_cost)) {
        $this->prorated_acc_costs = $prorater->prorateValue($accessorial_cost, $weights, 2);
      }
    }
    $this->use_costs = ($this->prorated_costs != -1);
    $this->use_acc_costs = ($this->prorated_acc_costs != -1);
  }

  /**
   * Override Base_Collection populate
   * @param  array $rows rows coming from DAO
   * @return object Billing_Payment_Extranet_Collection
   */
  public function populate($rows) {
    $this->models = array();

    if (!empty($rows)) {
      foreach ($rows as $row) {
        $model = $this->create_model($row);
        if ($model !== false) {
          $model->use_costs = $this->use_costs;
          $model->use_acc_costs = $this->use_acc_costs;
          $model->prorated_costs = $this->prorated_costs;
          $model->prorated_acc_costs = $this->prorated_acc_costs;
          $this->models[] = $model;
        }
      }
    }

    return $this;
  }
}