<?php
/**
 * Data content for billing payment item
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */

namespace WF\Shared\View_Classes\Fulfillment\billing_payment;

class Billing_Payment_Item_Data extends \WF\Extranet\Mustache\Mustache_Data {
  /**
   * @var \WF\Shared\Models\Overpack\Billing_Payment_Item_Model
   */
  public $billing_payment_item_model;

  /**
   * @return string Load ID
   */
  public function load_id() {
    return $this->billing_payment_item_model->load_id;
  }

  /**
   * @return int the identifier for the service agent attempt
   */
  public function saa_id() {
    return $this->billing_payment_item_model->saa_id;
  }

  /**
   * @return int Overpack load ID
   */
  public function opl_id() {
    return $this->billing_payment_item_model->opl_id;
  }

  /**
   * @return int Overpack load purchase order number including the store prefix
   */
  public function opl_po_num_send() {
    return $this->billing_payment_item_model->opl_po_num_send;
  }

  /**
   * @return int carrier reference number
   */
  public function opl_carrier_ref_number() {
    return $this->billing_payment_item_model->opl_carrier_ref_number;
  }

  /**
   * @return int Overpack load item ID
   */
  public function opi_id() {
    return $this->billing_payment_item_model->opi_id;
  }

  /**
   * @return int Overpack load item order product ID
   */
  public function opi_op_id() {
    return $this->billing_payment_item_model->opi_op_id;
  }

  /**
   * @return int Overpack load item quantity
   */
  public function opi_qty() {
    return $this->billing_payment_item_model->opi_qty;
  }

  /**
   * @return int Overpack load item carton count
   */
  public function opi_carton_count() {
    return $this->billing_payment_item_model->opi_carton_count;
  }

  /**
   * @return float Overpack load item corrected weight (OpiWeight * OpiQty)
   */
  public function opi_corrected_weight() {
    return round($this->billing_payment_item_model->opi_corrected_weight, 2);
  }

  /**
   * @return int Overpack load pallet weight
   */
  public function opl_pallet_weight() {
    return $this->billing_payment_item_model->opl_pallet_weight;
  }

  /**
   * @return string Overpack load received date
   */
  public function opl_received_date() {
    return $this->billing_payment_item_model->opl_received_date;
  }

  /**
   * @return int Overpack load item corrected carton count
   */
  public function opi_corrected_carton_count() {
    return $this->billing_payment_item_model->opi_corrected_carton_count;
  }

  /**
   * @return int Overpack load item type ID
   */
  public function opi_overpack_type_id() {
    return $this->billing_payment_item_model->opi_overpack_type_id;
  }

  /**
   * @return string Overpack load item cost in the specific currency format
   */
  public function opi_overpack_cost() {
    return format_currency($this->billing_payment_item_model->opi_overpack_cost, $this->ts_cuy_id());
  }

  /**
   * @return string Order product detail product name
   */
  public function od_pr_name() {
    return 'Name: ' . $this->billing_payment_item_model->od_pr_name;
  }

  /**
   * @return string Nanufacturer part number
   */
  public function pr_manu_part_num() {
    return $this->billing_payment_item_model->pr_manu_part_num;
  }

  /**
   * @return string Product SKU
   */
  public function pr_sku() {
    return $this->billing_payment_item_model->pr_sku;
  }

  /**
   * @return string The name of the option
   */
  public function opt_name() {
    return $this->billing_payment_item_model->opt_name;
  }

  /**
   * @return string The type of leg
   */
  public function leg_type() {
    return $this->billing_payment_item_model->leg_type;
  }

  /**
   * @return int Third party carrier ID
   */
  public function ts_id() {
    return $this->billing_payment_item_model->ts_id;
  }

  /**
   * @return string Currency ID
   */
  public function ts_cuy_id() {
    return $this->billing_payment_item_model->ts_cuy_id;
  }

  /**
   * @return string lnrs of Update
   */
  public function update() {
    return lnrs('Update', '', 'Update');
  }
}