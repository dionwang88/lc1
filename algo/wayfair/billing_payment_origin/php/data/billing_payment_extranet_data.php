<?php
/**
 * Data content for billing payment extranet
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */

namespace WF\Shared\View_Classes\Fulfillment\billing_payment;

require_once INCLUDE_PATH . '/includes/fn_lib_common.php';

class Billing_Payment_Extranet_Data extends \WF\Extranet\Mustache\Mustache_Data {

  /**
   * @var \WF\Shared\Models\Overpack\Billing_Payment_Extranet_Model
   */
  public $billing_payment_extranet_model;

  /**
   * @return array the items for a billing payment extranet row
   */
  public function billing_payment_items() {
    $items = [];
    foreach ($this->billing_payment_extranet_model->get_items() as $bpi) {
      $bpi_data = new Billing_Payment_Item_Data();
      $bpi_data->billing_payment_item_model = $bpi;
      $items[] = $bpi_data;
    }
    return $items;
  }

  /**
   * @return string Type of shipment
   */
  public function leg_type() {
    return $this->billing_payment_extranet_model->leg_type;
  }

  /**
   * @return string load id
   */
  public function load_id() {
    return $this->billing_payment_extranet_model->load_id;
  }


  /**
   * @return int load weight
   */
  public function load_weight() {
    return $this->billing_payment_extranet_model->load_weight;
  }

  /**
   * @return float load cost
   */
  public function load_cost() {
    return format_currency($this->billing_payment_extranet_model->load_cost, $this->ts_cuy_id());
  }

  /**
   * @return float PO overpack cost
   */
  public function po_overpack_cost() {
    return format_currency($this->billing_payment_extranet_model->po_overpack_cost, $this->ts_cuy_id());
  }

  /**
   * @return string PO status
   */
  public function po_status() {
    return $this->billing_payment_extranet_model->po_status;
  }

  /**
   * @return int the identifier for the service agent attempt
   */
  public function saa_id() {
    return $this->billing_payment_extranet_model->saa_id;
  }

  /**
   * @return int Shipping Load Manifest ID
   */
  public function slm_id() {
    return $this->billing_payment_extranet_model->slm_id;
  }

  /**
   * @return int Overpack load id
   */
  public function opl_id() {
    return $this->billing_payment_extranet_model->opl_id;
  }

  /**
   * @return int Overpack load purchase order number
   */
  public function opl_po_num() {
    return $this->billing_payment_extranet_model->opl_po_num;
  }

  /**
   * @return int carrier reference number
   */
  public function opl_carrier_ref_number() {
    return $this->billing_payment_extranet_model->opl_carrier_ref_number;
  }

  /**
   * @return string received date
   */
  public function opl_received_date() {
    $received_date = $this->billing_payment_extranet_model->opl_received_date;
    return date('m/d/Y', strtotime($received_date));
  }

  /**
   * @return int overpack load quantity (mpn count)
   */
  public function opl_mpn_count() {
    return $this->billing_payment_extranet_model->opl_mpn_count;
  }

  /**
   * @return int number of cartons
   */
  public function opl_carton_count() {
    return $this->billing_payment_extranet_model->opl_carton_count;
  }

  /**
   * @return int Total weight of the overpack load
   */
  public function opl_total_weight() {
    return $this->billing_payment_extranet_model->opl_total_weight;
  }

  /**
   * @return int overpack load pallet weight
   */
  public function opl_pallet_weight() {
    return $this->billing_payment_extranet_model->opl_pallet_weight;
  }

  /**
   * @return int overpack load purchase order number including the store prefix
   */
  public function opl_po_num_send() {
    return $this->billing_payment_extranet_model->opl_po_num_send;
  }

  /**
   * @return string scheduled delivery date
   */
  public function opl_delivery_scheduled_date() {
    return $this->billing_payment_extranet_model->opl_delivery_scheduled_date;
  }

  /**
   * @return string overpack load delivery received date
   */
  public function opl_delivery_received_date() {
    $received_date = $this->billing_payment_extranet_model->opl_delivery_received_date;
    return date('m/d/Y', strtotime($received_date));
  }

  /**
   * @return int Cost of any additional fees associated with shipping
   */
  public function accessorial_cost() {
    return format_currency($this->billing_payment_extranet_model->accessorial_cost, $this->ts_cuy_id());
  }

  /**
   * @return string overpack load item complete date
   */
  public function opi_complete_date() {
    return $this->billing_payment_extranet_model->opi_complete_date;
  }

  /**
   * @return int carrier id
   */
  public function ts_id() {
    return $this->billing_payment_extranet_model->ts_id;
  }

  /**
   * @return string currency id
   */
  public function ts_cuy_id() {
    $ts_currency_id = $this->billing_payment_extranet_model->ts_cuy_id;
    if (empty($ts_currency_id)) {
      $ts_currency_id = 'USD';
    }
    return $ts_currency_id;
  }

  /**
   * @return float total weight
   */
  public function total_weight() {
    $total_weight = $this->opl_total_weight() + $this->opl_pallet_weight();
    return round($total_weight, 2);
  }

  /**
   * @return string the total net pay after prorated
   */
  public function net_pay() {
    $use_costs = $this->billing_payment_extranet_model->use_costs;
    $prorated_costs = $this->billing_payment_extranet_model->prorated_costs;
    $po_num = $this->billing_payment_extranet_model->opl_po_num;
    $net_pay = $use_costs ? $prorated_costs[$po_num] : 0;
    return format_currency($net_pay, $this->ts_cuy_id());
  }

  /**
   * @return string the accessorial cost after prorated
   */
  public function acc_cost() {
    $prorated_acc_costs = $this->billing_payment_extranet_model->prorated_acc_costs;
    $use_acc_costs = $this->billing_payment_extranet_model->use_acc_costs;
    $po_num = $this->billing_payment_extranet_model->opl_po_num;
    $acc_cost = $use_acc_costs ? $prorated_acc_costs[$po_num] : 0;
    return format_currency($acc_cost, $this->ts_cuy_id());
  }

  /**
   * @return string the total cost after prorated cost
   */
  public function total_cost() {
    $use_costs = $this->billing_payment_extranet_model->use_costs;
    $prorated_costs = $this->billing_payment_extranet_model->prorated_costs;
    $po_num = $this->billing_payment_extranet_model->opl_po_num;
    $net_pay = $use_costs ? $prorated_costs[$po_num] : 0;

    $prorated_acc_costs = $this->billing_payment_extranet_model->prorated_acc_costs;
    $use_acc_costs = $this->billing_payment_extranet_model->use_acc_costs;
    $acc_cost = $use_acc_costs ? $prorated_acc_costs[$po_num] : 0;

    $overpack_cost = $this->billing_payment_extranet_model->po_overpack_cost;

    $total_cost = $net_pay + $acc_cost + $overpack_cost;

    return format_currency($total_cost, $this->ts_cuy_id());
  }

  /**
   * @return string load complete date
   */
  public function complete_date() {
    $leg_type = $this->leg_type();
    $receive_date = $this->opl_delivery_received_date();
    $opi_complete_date = '-';

    if ($leg_type == 'Customer Delivery') {
      if ($receive_date == '') {
        $po_complete_date = '-';
      } else {
        $po_complete_date = date('M d, Y', strtotime($receive_date));
      }
    } elseif ($leg_type == 'Attempted Delivery') {
      $po_complete_date = '-';
    } else {
      if ($opi_complete_date == '') {
        $po_complete_date = '-';
      } else {
        $po_complete_date = date('M d, Y', strtotime($opi_complete_date));
      }
    }

    return $opi_complete_date;
  }
}
