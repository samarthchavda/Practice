// /** @odoo-module **/
//
// import { registry } from "@web/core/registry";
// import { Component, useState } from "@odoo/owl";
//
// class Counter extends Component {
//     setup() {
//         this.state = useState({
//             count: 0,
//         });
//     }
//
//     increment() {
//         this.state.count++;
//     }
//
//     decrement(){
//         this.state.count--;
//     }
//
//     reset(){
//         this.state.count = 0;
//     }
// }
//
// Counter.template = "owl_practice.Counter";
//
// registry.category("actions").add("owl_practice.counter_action", Counter);