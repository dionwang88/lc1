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

class Overpack_Carrier_Data extends \WF\Extranet\Mustache\Mustache_Data {

  public $overpack_carrier;

  public function carrier_id() {
    return $this->overpack_carrier['carrier_id'];
  }

  public function carrier_name() {
    return $this->overpack_carrier['carrier_name'];
  }
}