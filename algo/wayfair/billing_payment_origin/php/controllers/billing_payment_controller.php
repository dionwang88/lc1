<?php
/**
 * Controller for the Billing and Payment tab on the Agent Extranet
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */
namespace WF\Extranet\Controllers\Overpack;

use WF\Extranet\View_Classes\Overpack\Billing_Payment\Billing_Payment_View;
use WF\Shared\Models\Overpack\Billing_Payment_Collection;
use WF\Shared\Models\Overpack\Billing_Payment_Extranet_Collection;
use WF\Shared\Models\Overpack\Billing_Payment_Item_Model;
use WF\Shared\Models\Overpack\Billing_Payment_Model;
use WF\Shared\View_Classes\Fulfillment\billing_payment\Billing_Payment_Data;
use WF\Shared\View_Classes\Fulfillment\billing_payment\Billing_Payment_Extranet_Data;
use WF\Shared\View_Classes\Fulfillment\billing_payment\Billing_Payment_Item_Data;

require_once INCLUDE_PATH . '/extranet/app_includes/overpack_functions.php';
require_once INCLUDE_PATH . '/includes/classes/finance/prorate/prorate_class.php';


class Billing_Payment_Controller extends \WF\Extranet\Controllers\Overpack\Base_Controller {

  /**
   * Creates the view for the initial loading of the screen
   *
   * @return \WF\Extranet\Controllers\Overpack\Billing_Payment_Controller
   */
  public function index() {
    $this->page_title = lnrs('BillingAndPayment', '', 'Billing And Payment');
    $billing_payment_view = new Billing_Payment_View();

    $billing_payment_collection = new Billing_Payment_Collection();
    $overpack_carrier_list = $billing_payment_collection->get_overpack_carrier_list();
    $billing_payment_view->overpack_carrier_list = $overpack_carrier_list;

    $this->content = $billing_payment_view;
  }

  /**
   * Loads all billing and payment to display on the page
   *
   * @return void
   */
  public function data() {
    $from_date = date("m/d/Y", strtotime($this->request('from_date')));
    $to_date = date("m/d/Y", strtotime($this->request('to_date')));
    $ts_id = $this->request('ts_id');
    $keyword = $this->request('keyword');
    $user_name = $this->request('user_name');
    $filter_by = $this->request('filter_by');
    $sort_by = $this->request('sort_by');
    $admin = $this->request('is_admin');

    $billing_payment_collection = $this->load_billing_payment($ts_id, $from_date, $to_date, $keyword, $user_name, $filter_by, $sort_by, $admin);
    $billing_payments = [];
    foreach ($billing_payment_collection as $i => $bill_payment) {
      $bp_data = new Billing_Payment_Data();
      $bp_data->billing_payment_model = $bill_payment;
      $bp_data->is_even = $i % 2 == 0;
      $billing_payments[] = $bp_data;
    }

    $this->content = $billing_payments;
  }

  /**
   * @param int    $ts_id     carrier id
   * @param string $from_date from date
   * @param string $to_date   to date
   * @param string $keyword   keyword
   * @param string $user_name log in user name
   * @param string $filter_by filter by field
   * @param string $sort_by   sort by field
   * @param int    $admin     is admin or not
   *
   * @return object Billing_Payment_Collection
   */
  private function load_billing_payment($ts_id, $from_date, $to_date, $keyword, $user_name, $filter_by, $sort_by, $admin) {
    if ($keyword === '') {
      $keyword = null;
    }
    if ($user_name === '') {
      $user_name = null;
    }

    if ($filter_by === '') {
      $filter_by = null;
    }

    if ($sort_by === '') {
      $sort_by = null;
    }

    if (!empty($keyword)) {
      $to_date_for_sql = '';
      $from_date_for_sql = '';
    } else {
      $to_date_for_sql = format_date_db(adjust_extranet_date('+1 day', $to_date)); //Consider all billing happened on the given day as well
      $from_date_for_sql = format_date_db($from_date);
    }
    $billing_payment_collection = new Billing_Payment_Collection();
    $billing_payment_collection->load_billing_payment($from_date_for_sql, $to_date_for_sql, $ts_id, $keyword, $user_name, $admin, $filter_by, $sort_by);
    return $billing_payment_collection;
  }

  /**
   * Loads the billing and payment by po
   * @return object $this->content
   */
  public function get_extranet_data() {
    $saa_id = $this->request('saa_id');
    $slm_id = $this->request('slm_id');

    $billing_payment_extranet_collection = new Billing_Payment_Extranet_Collection();
    $billing_payment_extranet_collection->load_billing_payment_extranet($saa_id, $slm_id);

    $extranets = [];
    foreach ($billing_payment_extranet_collection as $bpe) {
      $bpe_data = new Billing_Payment_Extranet_Data();
      $bpe_data->billing_payment_extranet_model = $bpe;
      $extranets[] = $bpe_data;
    }

    $this->content = $extranets;
  }

  /**
   * Update Carton Information for a billing and payment item
   * @return object $this->content
   */
  public function update() {
    $opi_id = $this->request('opi_id');
    $opl_id = $this->request('opl_id');
    $opi_carton_count = $this->request('opi_corrected_carton_count');
    $opi_weight = $this->request('opi_corrected_weight');
    $leg_type = $this->request('leg_type');
    $opi_approved = $this->request('askForApproval');
    if ($opi_approved === null || $opi_approved === '') {
      $opi_approved = 0;
    }

    $billing_payment_item_model = new Billing_Payment_Item_Model();
    $net_pay = $billing_payment_item_model->update_carton_count($opi_id, $opl_id, $opi_carton_count, $opi_weight, $leg_type, $opi_approved);
    $this->content = $net_pay;
  }

  /**
   * Update the status for the checked billing and payment rows
   * @return object $this->content
   */
  public function update_status_to_approved() {
    $slm_ids = $this->request('slm_ids');
    $saa_ids = $this->request('saa_ids');

    $from_date = date("m/d/Y", strtotime($this->request('fromDate')));
    $to_date = date("m/d/Y", strtotime($this->request('toDate')));
    $ts_id = $this->request('carrier');
    $keyword = $this->request('keyword');
    $user_name = $this->request('userName');
    $filter_by = $this->request('filterBy');
    $sort_by = $this->request('sortBy');
    $admin = $this->request('is_admin');

    $slm_ids_array = null;
    $saa_ids_array = null;

    if ($slm_ids != null and strlen($slm_ids) != 0) {
      $slm_ids_arr = explode(',', $slm_ids);
      $slm_ids_array = [];
      foreach ($slm_ids_arr as $slm_id) {
        $slm_ids_array[] = intval($slm_id);

      }
    }

    if ($saa_ids != null and strlen($saa_ids) != 0) {
      $saa_ids_arr = explode(',', $saa_ids);
      $saa_ids_array = [];
      foreach ($saa_ids_arr as $saa_id) {
        $saa_ids_array[] = intval($saa_id);
      }
    }

    $billing_payment_collection = new Billing_Payment_Collection();
    $billing_payment_collection->update_status_to_approved($slm_ids_array, $saa_ids_array);

    $billing_payment_collection = $this->load_billing_payment($ts_id, $from_date, $to_date, $keyword, $user_name, $filter_by, $sort_by, $admin);

    $slm_lock_text = [];
    $saa_lock_text = [];
    if (!empty($slm_ids_array)) {
      foreach ($slm_ids_array as $slm_id) {
        foreach ($billing_payment_collection as $bill_payment) {
          $bp_data = new Billing_Payment_Data();
          $bp_data->billing_payment_model = $bill_payment;
          if ($slm_id === $bp_data->slm_id()) {
            $new_arr = [];
            $new_arr['slm_id'] = $slm_id;
            $new_arr['lock_text'] = $bp_data->locked_text();
            $slm_lock_text[] = $new_arr;
          }
        }
      }
    }
    if (!empty($saa_ids_array)) {
      foreach ($saa_ids_array as $saa_id) {
        foreach ($billing_payment_collection as $bill_payment) {
          $bp_data = new Billing_Payment_Data();
          $bp_data->billing_payment_model = $bill_payment;
          if ($saa_id === $bp_data->saa_id()) {
            $new_arr = [];
            $new_arr['saa_id'] = $saa_id;
            $new_arr['lock_text'] = $bp_data->locked_text();
            $saa_lock_text[] = $new_arr;
          }
        }
      }
    }
    $this->content = ['slm_lock_text' => $slm_lock_text, 'saa_lock_text' => $saa_lock_text];
  }

  /**
   * Get the detail of the billing payment accessorials
   * @return object $this->content
   */
  public function get_billing_accessorials() {
    $slm_id = $this->request('slm_id');
    $saa_id = $this->request('saa_id');

    $billing_payment_model = new Billing_Payment_Model();
    $results = $billing_payment_model->get_billing_accessorials($slm_id, $saa_id);
    $success = true;
    if (empty($results)) {
      $results = [];
      $success = false;
    }

    $this->content = ['success' => $success, 'results' => $results];
  }
}