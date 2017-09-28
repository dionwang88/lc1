<?php
/**
 * Data content for billing payment
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */

namespace WF\Shared\View_Classes\Fulfillment\billing_payment;

require_once INCLUDE_PATH . '/includes/fn_lib_common.php';

class Billing_Payment_Data extends \WF\Extranet\Mustache\Mustache_Data {

  /**
   * @var \WF\Shared\Models\Overpack\Billing_Payment_Model
   */
  public $billing_payment_model;

  /**
   * @return string po summary for a billing and payment row
   */
  public function po_details() {
    $current_agent = $this->sva_name();
    $current_load_id = preg_replace('/\s+/', '', $this->carrier_ref());

    $ship_speed_edi_code = $this->ship_speed_edi_code();
    if ($ship_speed_edi_code == 'WGB') {
      $service_type = lnrs('Threshold', '', 'Threshold');
    } elseif ($ship_speed_edi_code == 'WGS') {
      $service_type = lnrs('RoomOfChoice', '', 'Room of Choice');
    } elseif ($ship_speed_edi_code == 'WGG' || $ship_speed_edi_code == 'WGP') {
      $service_type = lnrs('WhiteGlove', '', 'White Glove');
    } elseif ($ship_speed_edi_code == 'NULL') {
      $service_type = '';
    } else {
      $service_type = lnrs('Standard', '', 'Standard');
    }
    $service_type = empty($service_type) ? '' : ' - ' . $service_type;

    return $current_agent . ' - ' . $current_load_id . $service_type;
  }

  /**
   * @return int whether is admin or not
   */
  public function is_admin() {
    if (session('admin_loggedin') && session('extranetUserName') == '') {
      //admin logged in as a wayfair employee
      $admin = 1;
    } else {
      //either admin logged in as agent or actual agent is logged in
      $admin = 0;
    }
    return $admin;
  }

  /**
   * @return int Shipping Load Manifest ID
   */
  public function slm_id() {
    return $this->billing_payment_model->slm_id;
  }

  /**
   * @return int Carrier Reference Number
   */
  public function carrier_ref() {
    return $this->billing_payment_model->carrier_ref;
  }

  /**
   * @return int A special EDI (electronic data interchange) code
   */
  public function ship_speed_edi_code() {
    return $this->billing_payment_model->ship_speed_edi_code;
  }

  /**
   * @return string load complete date format mm/dd/yyyy
   */
  public function load_complete_date() {
    $load_complete_date = $this->billing_payment_model->load_complete_date;
    if ($load_complete_date == '') {
      $load_complete_date = '-';
    }
    return date('m/d/Y', strtotime($load_complete_date));
  }

  /**
   * @return string load pickup date format mm/dd/yyyy
   */
  public function load_pickup_date() {
    $pick_up_date = $this->billing_payment_model->load_pickup_date;

    if ($pick_up_date == '') {
      $received_date = '-';
    } else {
      $received_date = $pick_up_date;
    }

    return date('m/d/Y', strtotime($received_date));
  }

  /**
   * @return int load purchase order count
   */
  public function load_po_count() {
    return $this->billing_payment_model->load_po_count;
  }

  /**
   * @return float load overpack cost
   */
  public function load_overpack_cost() {
    return format_currency($this->billing_payment_model->load_overpack_cost, $this->ts_cuy_id());
  }

  /**
   * @return int load quantity
   */
  public function load_qty() {
    return $this->billing_payment_model->load_qty;
  }

  /**
   * @return int the total number of boxes
   */
  public function load_carton() {
    return $this->billing_payment_model->load_carton;
  }

  /**
   * @return float load weight
   */
  public function load_weight() {
    $load_weight = $this->billing_payment_model->load_weight;
    $slm_pallet_weight = $this->slm_pallet_weight();
    return round($load_weight + $slm_pallet_weight, 2);
  }

  /**
   * @return int the identifier for the service agent attempt
   */
  public function saa_id() {
    return $this->billing_payment_model->saa_id;
  }

  /**
   * @return int leg_type_id
   */
  public function leg_type_id() {
    return $this->billing_payment_model->leg_type_id;
  }

  /**
   * @return string leg_type
   */
  public function leg_type_name() {
    return $this->get_leg_type($this->leg_type_id());
  }

  /**
   * Mapping the leg_type_id to leg_type
   *
   * @param  int $id leg type id
   * @return string
   */
  private function get_leg_type($id) {
    switch ($id) {
      case 0:
        return lnrs('CustomerDelivery', '', 'Customer Delivery');
      break;
      case 1:
        return lnrs('SupplierPickup', '', 'Supplier Pickup');
      break;
      case 2:
        return lnrs('AttemptedPickup', '', 'Attempted Pickup');
      break;
      case 3:
        return lnrs('AttemptedDelivery', '', 'Attempted Delivery');
      break;
      case 4:
        return lnrs('CrossdockFee', '', 'Crossdock Fee');
      break;
      default:
        return lnrs('Unknown', '', 'Unknown');
      break;
    }
  }

  /**
   * @return string load paid status
   */
  public function load_paid_status() {
    return $this->billing_payment_model->load_paid_status;
  }

  /**
   * @return string load status
   */
  public function load_status() {
    $load_status = $this->billing_payment_model->load_status;
    if ($this->load_paid_status() == 1) {
      $load_status = 'Paid';
    }
    return $load_status;
  }

  /**
   * @return float load cost
   */
  public function load_cost() {
    return format_currency($this->billing_payment_model->load_cost, $this->ts_cuy_id());
  }

  /**
   * @return int load miles
   */
  public function load_miles() {
    $num_miles = '-';
    $load_miles = $this->billing_payment_model->load_miles;
    if (!empty($load_miles) && $load_miles > 0) {
      $num_miles = $load_miles;
    }
    return $num_miles;
  }

  /**
   * @return string Service Agent Name
   */
  public function sva_name() {
    return $this->billing_payment_model->sva_name;
  }

  /**
   * @return int Service Agent ID
   */
  public function sva_id() {
    return $this->billing_payment_model->sva_id;
  }

  /**
   * @return int the Third Party Carrier Code
   */
  public function ts_ctl_carrier_code() {
    return $this->billing_payment_model->ts_ctl_carrier_code;
  }

  /**
   * @return float the Cost for any Accessorials (extra stuff other than the normal pickup/shipment cost)
   */
  public function accessorial_cost() {
    return format_currency($this->billing_payment_model->accessorial_cost, $this->ts_cuy_id());
  }

  /**
   * @return bool a bit flag to denote that the payment has been rejected, but I am not 100% sure about this one.
   */
  public function is_fully_rejected() {
    return $this->billing_payment_model->is_fully_rejected;
  }

  /**
   * @return float shipping load manifest pallet weight
   */
  public function slm_pallet_weight() {
    return $this->billing_payment_model->slm_pallet_weight;
  }

  /**
   * @return int carrier id
   */
  public function ts_id() {
    return $this->billing_payment_model->ts_id;
  }

  /**
   * @return string the currency id
   */
  public function ts_cuy_id() {
    return $this->billing_payment_model->ts_cuy_id;
  }

  /**
   * @return float transportation cost threshold
   */
  public function ts_transportation_cost_threshold() {
    return $this->billing_payment_model->ts_transportation_cost_threshold;
  }

  /**
   * @return float Retrieve the Total Cost
   */
  public function total_cost() {
    $load_cost = $this->billing_payment_model->load_cost;
    $load_overpack_cost = $this->billing_payment_model->load_overpack_cost;
    $accessorial_cost = $this->billing_payment_model->accessorial_cost;
    $total_cost = $load_cost + $load_overpack_cost + $accessorial_cost;

    return format_currency($total_cost, $this->ts_cuy_id());
  }

  /**
   * @return string the displayed name on the Action field
   */
  public function locked_text() {
    $locked_text = 'Show';
    $locked_status_array = array('Invoiced', 'Approved', 'Paid');

    if (feature_check(2829272, 100, 'Do not allow expanding of Awaiting Inspection status')) {
      array_push($locked_status_array, 'Awaiting Inspection');
    }
    $load_status = $this->load_status();
    $threshold = $this->ts_transportation_cost_threshold();
    $total_cost = $this->total_cost();

    if (in_array($load_status, $locked_status_array)) {
      // load is invoiced or approved
      $locked_text = 'Locked';
    } elseif ($load_status == 'Open') {
      // some activity is yet to complete
      $locked_text = 'Show';
    } elseif (($load_status == 'Review') || (($load_status == 'Complete') && ($threshold) && ($total_cost >= $threshold))) {
      //If in case it was not in review but threshold value condition is matched we set it to 'Review' for the rest of the web page
      $load_status = 'Review';
      $admin = session('admin_loggedin');
      if ($admin == 1) {
        $locked_text = 'Needs Approval';
      } else {
        $locked_text = 'Show';
      }
    }
    return $locked_text;
  }

  /**
   * @return string the class for locked_text on the web page
   */
  public function locked_text_class() {
    return ($this->locked_text() === 'Locked' && $this->load_paid_status() == 0) ? '' : 'js-action-list-show';
  }

  /**
   * @return string the style for locked_text on the web page
   */
  public function locked_text_style() {
    return ($this->locked_text() === 'Locked' && $this->load_paid_status() == 0) ? '' : 'text-decoration:underline;cursor:pointer';
  }

  /**
   * @return bool the flag to show link
   */
  public function show_link_flag() {
    $show_link = false;
    $is_fully_rejected = $this->is_fully_rejected();
    $accessorial_cost = $this->billing_payment_model->accessorial_cost;
    if ($accessorial_cost > 0 || $is_fully_rejected) {
      $show_link = true;
    }
    return $show_link;
  }

  /**
   * Whether the billing and payment load is completed
   * @return bool
   */
  public function load_completed_flag() {
    return $this->load_status() == 'Complete';
  }

  /**
   * return true: checkbox id and value are all $slm_id, name is slm_approved[]
   * return false: checkbox id and value are all $saa_id, name is saa_approved[]
   * @return bool
   */
  public function checkbox_type_flag() {
    if ($this->slm_id() > 0) {
      return true;
    } else {
      return false;
    }
  }

  /**
   * @var bool control the color of the row
   */
  public $is_even;
  /**
   * Control the row color, even or odd
   * @return bool
   */
  public function is_even() {
    return $this->is_even;
  }
  /**
   * The template this data is associated with
   *
   * @return string The template name
   */
  protected function template_name() {
    // No template
    return '';
  }
}
