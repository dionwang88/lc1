<?php
/**
 * View for the Billing and Payment tab on the Agent Extranet
 *
 * PHP version 5
 *
 * @author    Qian Wang <qwang@wayfair.com>
 * @copyright 2016 Wayfair LLC - All rights reserved
 */

namespace WF\Extranet\View_Classes\Overpack\Billing_Payment;

use WF\Shared\Mustache\Tungsten_Data;

require_once INCLUDE_PATH . '/extranet/app_includes/overpack_functions.php';

class Billing_Payment_View extends \WF\Extranet\Mustache\Mustache_Data {
  use WF\Shared\Mustache\Tungsten_Data;

  /**
   * Constructs the HTML for the tab navigation on the extranet
   *
   * @return string HTML for the tabs
   */
  public function tab_nav() {
    return create_tab_nav(\OverpackStatus::BillingAndPayment);
  }

  /**
   * @var object Billing_Payment_Collection
   */
  public $billing_payment_collection;

  /**
   * @var array overpack carrier id list
   */
  public $overpack_carrier_list;

  /**
   * @return array overpack carrier id list
   */
  public function overpack_carrier_list() {
    return $this->overpack_carrier_list;
  }

  /**
   * @return object Billing_Payment_Collection
   */
  public function billing_payment_collection() {
    return $this->billing_payment_collection;
  }
  /**
   * Retrieves the lnrs for BillingAndPayment
   *
   * @return string lnrs for BillingAndPayment
   */
  public function lnrs_billing_payment() {
    return lnrs('BillingAndPayment', '', 'Billing And Payment');
  }

  /**
   * Retrieves the lnrs for Keywords
   *
   * @return string lnrs for Keywords
   */
  public function lnrs_keywords() {
    return lnrs('Keywords', '', 'Keywords: ');
  }

  /**
   * Retrieves the lnrs for FilterBy
   *
   * @return string lnrs for FilterBy
   */
  public function lnrs_filter_by() {
    return lnrs('FilterBy', '', 'Filter By: ');
  }

  /**
   * Retrieves the lnrs for unpaid
   *
   * @return string lnrs for unpaid
   */
  public function lnrs_unpaid() {
    return lnrs('Unpaid', '', 'Unpaid');
  }
  /**
   * Retrieves the lnrs for Open
   *
   * @return string lnrs for Open
   */
  public function lnrs_open() {
    return lnrs('Open', '', 'Open');
  }

  /**
   * Retrieves the lnrs for Complete
   *
   * @return string lnrs for Complete
   */
  public function lnrs_complete() {
    return lnrs('Complete', '', 'Complete');
  }

  /**
   * Retrieves the lnrs for Approved
   *
   * @return string lnrs for Approved
   */
  public function lnrs_approved() {
    return lnrs('Approved', '', 'Approved');
  }
  /**
   * Retrieves the lnrs for Invoiced
   *
   * @return string lnrs for Invoiced
   */
  public function lnrs_invoiced() {
    return lnrs('Invoiced', '', 'Invoiced');
  }
  /**
   * Retrieves the lnrs for Review
   *
   * @return string lnrs for Review
   */
  public function lnrs_review() {
    return lnrs('Review', '', 'Review');
  }
  /**
   * Retrieves the lnrs for paid
   *
   * @return string lnrs for paid
   */
  public function lnrs_paid() {
    return lnrs('Paid', '', 'Paid');
  }
  /**
   * Retrieves the lnrs for Sort By
   *
   * @return string lnrs for Sort By
   */
  public function lnrs_sort_by() {
    return lnrs('SortBy', '', 'Sort By: ');
  }

/**
 * Retrieves the lnrs for PO Details on Sort By
 * @return string lnrs for PO Details
 */
  public function lnrs_po_details() {
    return lnrs('PoDetails', '', 'PO Details');
  }
  /**
   * Retrieves the lnrs for Reference Number
   *
   * @return string lnrs for Reference Number
   */
  public function lnrs_reference_number() {
    return lnrs('ReferenceNumber', '', 'Reference Number');
  }
  /**
   * Retrieves the lnrs for Total Weight
   *
   * @return string lnrs for Total Weight
   */
  public function lnrs_total_weight() {
    return lnrs('TotalWeight', '', 'Total Weight');
  }
  /**
   * Retrieves the lnrs for Transportation Cost
   *
   * @return string lnrs for Transportation Cost
   */
  public function lnrs_transportation_cost() {
    return lnrs('TransportationCost', '', 'Transportation Cost');
  }
  /**
   * Retrieves the lnrs for Total Cost
   *
   * @return string lnrs for Total Cost
   */
  public function lnrs_total_cost() {
    return lnrs('TotalCost', '', 'Total Cost');
  }
  /**
   * Retrieves the lnrs for Complete Date
   *
   * @return string lnrs for Complete Date
   */
  public function lnrs_complete_date() {
    return lnrs('CompleteDate', '', 'Complete Date');
  }

 /**
 * Retrieves the lnrs for From Calendar
 *
 * @return string lnrs for From Calendar Object
 */
  public function from_date() {
    $from_date = date('Y/m/d', strtotime('-1 Month'));
    return generate_calendar_html('from_date', 'from_date', $from_date, '', true, true, ['wfe_input js-bp-from-date']);
  }
 /**
 * Retrieves the lnrs for To Calendar
 *
 * @return string lnrs for To Calendar Object
 */
  public function to_date() {
    $to_date = date('Y/m/d');
    return generate_calendar_html('to_date', 'to_date', $to_date, '', true, true, ['wfe_input js-bp-to-date']);
  }
/**
 * Retrieves the lnrs for From Date
 *
 * @return string lnrs for From Date
 */
  public function lnrs_from_date() {
    return lnrs('FromDate', '', 'From Date: ');
  }
/**
 * Retrieves the lnrs for To Date
 *
 * @return string lnrs for To Date
 */
  public function lnrs_to_date() {
    return lnrs('ToDate', '', 'To Date: ');
  }
  /**
   * Retrieves the lnrs for Carrier
   *
   * @return string lnrs for Carrier
   */
  public function lnrs_carrier() {
    return lnrs('Carrier', '', 'Carrier: ');
  }
  /**
   * Retrieves the lnrs for Carrier List
   *
   * @return string lnrs for Carrier List
   */
  public function lnrs_carrier_list() {
    return generate_overpack_carrier_list(0);
  }

  /**
   * Retrieves the lnrs for Search
   *
   * @return string lnrs for Search
   */
  public function lnrs_search() {
    return lnrs('Search', '', 'Search');
  }

  /**
   * check whether the user is admin or not
   * return int 1 : is admin, 0: not admin
   * @return int
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
   * Get the extranet user name
   * @return string : extranet user name
   */
  public function user_name() {
    $extranet_user_name = '';
    if (session('admin_loggedin')) {
      $extranet_user_name = session('extranetUserName') != '' ? session('extranetUserName') : '';
    } elseif (session('extranetuser_loggedin')) {
      $extranet_user_name = session('extranetUserName');
    }
    return $extranet_user_name;
  }
  /**
   * Retrieves the lnrs for Export As
   * @return string Export As
   */
  public function export_as() {
    return lnrs('ExportAsColon', '', 'Export as:');
  }

  /**
   * Retrieves the URL for the loading icon
   *
   * @return string URL for the loading icon
   */
  public function loading_icon() {
    return STTCommon . 'st4/stores/common/wayfair_loading_big.gif';
  }

  /**
   * @return string lnrs of Approve Invoice
   */
  public function approve_invoice() {
    return lnrs('ApproveInvoices', '', 'Approve Invoices');
  }

  /**
   * Retrieves the lnrs for a server error message when printing PDFs
   *
   * @return string lnrs for the server error message when printing PDFs
   */
  public function lnrs_server_error() {
    return lnrs(
        'AnErrorOccurredWhileGeneratingThePDFPeriodPleaseCloseTheModalAndTryAgainPeriod',
        '',
        'An error occurred while generating the PDF. Please close the modal and try again.'
    );
  }

  /**
   * CSS files to include on the page
   *
   * @return array Array of css files to include
   */
  public function css() {
    return ['overpack'];
  }

  /**
   * CSS files to include on the page
   *
   * @return array Array of css files to include
   */
  public function sass() {
    return ['billing_payment', 'shipping_documents_print_center'];
  }

  /**
   * Defines the tungsten view
   *
   * @return string The tungsten view module
   */
  protected function tungsten_view_module() {
    return 'billing_payment_app_view';
  }

  /**
   * Defines the tungsten model
   *
   * @return string The tungsten model module
   */
  protected function tungsten_model_module() {
    return 'billing_payment_app_model';
  }

  /**
   * The template this data is associated with
   *
   * @return string The template name
   */
  protected function template_name() {
    return 'overpack/billing_payment/billing_payment';
  }
}
