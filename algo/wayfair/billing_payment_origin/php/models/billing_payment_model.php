<?php
/**
 * The Billing Payment Model
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */

namespace WF\Shared\Models\Overpack;

use WF\Shared\DAOs\Overpack\Billing_Payment_DAO;
use WF\Shared\Logging\Logger;

class Billing_Payment_Model extends \WF\Shared\Models\Base_Model {

  /**
   * @var int Shipping Load Manifest ID
   */
  public $slm_id;

  /**
   * @var int Carrier Reference Number
   */
  public $carrier_ref;

  /**
   * @var int A special EDI (electronic data interchange) code
   */
  public $ship_speed_edi_code;

  /**
   * @var string load complete date
   */
  public $load_complete_date;

  /**
   * @var string load pickup date
   */
  public $load_pickup_date;

  /**
   * @var int load purchase order count
   */
  public $load_po_count;

  /**
   * @var float load overpack cost
   */
  public $load_overpack_cost;

  /**
   * @var int load quantity
   */
  public $load_qty;

  /**
   * @var int the total number of boxes
   */
  public $load_carton;

  /**
   * @var  float total load weight
   */
  public $load_weight;

  /**
   * @var int the identifier for the service agent attempt
   */
  public $saa_id;

  /**
   * @var int leg_type_id
   */
  public $leg_type_id;

  /**
   * @var string load paid status
   */
  public $load_paid_status;

  /**
   * @var string load status
   */
  public $load_status;

  /**
   * @var float load total cost
   */
  public $load_cost;

  /**
   * @var int load miles
   */
  public $load_miles;

  /**
   * @var string Service Agent Name
   */
  public $sva_name;

  /**
   * @var int Service Agent ID
   */
  public $sva_id;

  /**
   * @var int the Third Party Carrier Code
   */
  public $ts_ctl_carrier_code;

  /**
   * @var float the Cost for any Accessorials (extra stuff other than the normal pickup/shipment cost)
   */
  public $accessorial_cost;

  /**
   * @var bool a bit flag to denote that the payment has been rejected, but I am not 100% sure about this one.
   */
  public $is_fully_rejected;

  /**
   * @var float shipping load manifest pallet weight
   */
  public $slm_pallet_weight;

  /**
   * @var int carrier id
   */
  public $ts_id;

  /**
   * @var string the currency id
   */
  public $ts_cuy_id;

  /**
   * @var float transportation cost threshold
   */
  public $ts_transportation_cost_threshold;

  /**
   * The Logger instance
   *
   * @var \WF\Shared\Logging\Logger
   */
  private $logger;

  /**
   * The DAO
   *
   * @var \WF\Shared\DAOs\Overpack\Billing_Payment_DAO
   */
  protected $dao;

  /**
   * Get the Logger instance
   *
   * @return \WF\Shared\Logging\Logger the Logger instance
   */
  private function get_logger() {
    if (!isset($this->logger)) {
      $this->logger = Logger::use_logger('Delivery_Route_Model');
    }

    return $this->logger;
  }

  /**
   * Constructor
   * 
   * @param null $dao Billing_Payment_Dao
   */
  public function __construct($dao = null) {
    parent::__construct($dao ?: new Billing_Payment_DAO());
  }

  /**
   * Populate this model from a map
   *
   * @param array $map the map
   *
   * @return \WF\Shared\Models\Overpack\Billing_Payment_Model|bool the populated model or false if there was an error
   */
  public function populate($map) {
    if (empty($map)) {
      return false;
    }
    parent::populate($map);
    $this->slm_id = $map['SlmID'];
    $this->saa_id = $map['SaaID'];
    $this->sva_name = $map['SvaName'];
    $this->sva_id = $map['SvaID'];
    $this->ts_ctl_carrier_code = $map['TsCTLCarrierCode'];
    $this->slm_pallet_weight = $map['SlmPalletWeight'];
    $this->ts_id = $map['TsID'];
    $this->ts_cuy_id = $map['TsCuyID'];
    $this->ts_transportation_cost_threshold = $map['TsTransportationCostThreshold'];
    return $this;
  }

  /**
   * Get the accessorial costs details of the billing payment
   *
   * @param int $slm_id slm id
   * @param int $saa_id saa id
   *
   * @return array
   */
  public function get_billing_accessorials($slm_id, $saa_id) {
    return $this->dao->get_billing_accessorials($slm_id, $saa_id);
  }
}
