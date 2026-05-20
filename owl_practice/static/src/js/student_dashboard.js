/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class StudentDashboard extends Component {
    static template = "owl_practice.StudentDashboard";

    setup() {
        this.orm = useService("orm");
        this.action = useService("action")

        this.state = useState({
            totalStudents: 0,
            students: [],
            showStudents: false,
        });

        onWillStart(async () => {
            this.state.totalStudents = await this.orm.searchCount("student.deatils", []);
        });


    }

    openStudentList() {
    this.action.doAction({
        type: "ir.actions.act_window",
        name: "Student Details",
        res_model: "student.deatils",
        view_mode: "list,form",
        views: [[false, "list"], [false, "form"]],
        target: "current",
    });
}

    async showStudentDetails() {
        this.state.students = await this.orm.searchRead(
            "student.deatils",
            [],
            ["name", "roll_no", "sport_ids"]
        );

        this.state.showStudents = true;
    }
}

registry.category("actions").add("owl_practice.student_dashboard", StudentDashboard);