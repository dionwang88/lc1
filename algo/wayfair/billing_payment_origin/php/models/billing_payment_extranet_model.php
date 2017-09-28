<?php
/**
 * The Extranet Billing Payment Model
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */
namespace WF\Shared\Models\Overpack;

use WF\Shared\DAOs\Overpack\Billing_Payment_DAO;

class Billing_Payment_Extranet_Model extends \WF\Shared\Models\Base_Model {

  /**
   * @var string Type of shipment
   */
  public $leg_type;

  /**
   * @var string Load id
   */
  public $load_id;

  /**
   * @var int Load weight
   */
  public $load_weight;

  /**
   * @var float Load cost
   */
  public $load_cost;

  /**
   * @var float Purchase order overpack cost
   */
  public $po_overpack_cost;

  /**
   * @var string Purchase order status
   */
  public $po_status;

  /**
   * @var int Identifier for the service agent attempt
   */
  public $saa_id;

  /**
   * @var int Shipping load manifest id
   */
  public $slm_id;

  /**
   * @var int Overpack load id
   */
  public $opl_id;

  /**
   * @var int Overpack load purchase order number
   */
  public $opl_po_num;

  /**
   * @var int Carrier reference number
   */
  public $opl_carrier_ref_number;

  /**
   * @var string Overpack load receive date
   */
  public $opl_received_date;

  /**
   * @var int Overpack load quantity (mpn count)
   */
  public $opl_mpn_count;

  /**
   * @var int Overpack load carton count
   */
  public $opl_carton_count;

  /**
   * @var int Total weight of the overpack load
   */
  public $opl_total_weight;

  /**
   * @var int Overpack load pallet weight
   */
  public $opl_pallet_weight;

  /**
   * @var int Overpack load purchase order number including the store prefix
   */
  public $opl_po_num_send;

  /**
   * @var string Scheduled delivery date
   */
  public $opl_delivery_scheduled_date;

  /**
   * @var string Overpack load delivery received date
   */
  public $opl_delivery_received_date;

  /**
   * @var int Cost of any additional fees associated with shipping
   */
  public $accessorial_cost;

  /**
   * @var string Overpack load item complete date
   */
  public $opi_complete_date;

  /**
   * @var int Carrier id
   */
  public $ts_id;

  /**
   * @var string Currency id
   */
  public $ts_cuy_id;

  /**
   * @var object Billing_Payment_Item_Collection
   */
  public $bp_item_collection;

  /**
   * @var int Temp variable for compute model cost coming from extranet collection
   */
  public $use_costs;
  /**
   * @var int Temp variable for compute model cost coming from extranet collection
   */
  public $use_acc_costs;
  /**
   * @var int Temp variable for compute model cost coming from extranet collection
   */
  public $prorated_costs;
  /**
   * @var int Temp variable for compute model cost coming from extranet collection
   */
  public $prorated_acc_costs;
  /**
   * The DAO
   *
   * @var \WF\Shared\DAOs\Overpack\Billing_Payment_DAO
   */
  protected $dao;

  /**
   * Constructor of Billing_Payment_Extranet_Model
   *
   * @param object $dao Billing_Payment_DAO
   */
  public function __construct($dao = null) {
    parent::__construct($dao ?: new Billing_Payment_DAO());
    $this->bp_item_collection = new Billing_Payment_Item_Collection();
  }

  /**
   * Loads billing and payment extranet items from DB
   * @return null
   */
  public function load_items() {
    $this->bp_item_collection->load_billing_payment_item($this->saa_id, $this->slm_id, $this->opl_id);
  }

  /**
   * @return array billing and payment extranet items
   */
  public function get_items() {
    return $this->bp_item_collection->get();
  }

  /**
   * Populate this model from a map
   *
   * @param array $map the map
   *
   * @return \WF\Shared\Models\Overpack\Billing_Payment_Extranet_Model|bool the populated model or false if there was an error
   */
  public function populate($map) {
    if (empty($map)) {
      return false;
    }
    parent::populate($map);

    $this->saa_id = $map['SaaID'];
    $this->slm_id = $map['SlmID'];
    $this->opl_id = $map['OplID'];
    $this->opl_po_num = $map['OplPoNum'];
    $this->opl_carrier_ref_number = $map['OplCarrierRefNumber'];
    $this->opl_received_date = $map['OplReceivedDate'];
    $this->opl_mpn_count = $map['OplMpnCount'];
    $this->opl_carton_count = $map['OplCartonCount'];
    $this->opl_total_weight = $map['OplTotalWeight'];
    $this->opl_pallet_weight = $map['OplPalletWeight'];
    $this->opl_po_num_send = $map['OplPoNumSend'];
    $this->opl_delivery_scheduled_date = $map['OplDeliveryScheduledDate'];
    $this->opl_delivery_received_date = $map['OplDeliveryReceivedDate'];
    $this->accessorial_cost = $map['accessorial_cost'];
    $this->opi_complete_date = $map['OpiCompleteDate'];
    $this->ts_id = $map['TsID'];
    $this->ts_cuy_id = $map['TsCuyID'];

    $this->load_items();
    return $this;
  }
}
