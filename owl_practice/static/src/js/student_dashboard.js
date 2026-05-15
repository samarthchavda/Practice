/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class StudentDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.notification = useService("notification");

        this.state = useState({
            students: [],
            name: "",
            phone: "",
            nationality:"indian ",
        });

        onWillStart(async () => {
            this.state.sports = await this.orm.searchRead(
                "student.sports",
                [],
                ["name"]
            );
            await this.loadStudents();
        });
    }

    async loadStudents() {
        this.state.students = await this.orm.searchRead(
            "student.deatils",
            [],
            ["name", "phone","nationality"]
        );
    }

    async createStudent() {
        if (!this.state.name || !this.state.phone) {
            this.notification.add("Please fill all details", {
                type: "danger",
            });
            return;
        }

        await this.orm.create("student.deatils", [{
            name: this.state.name,
            phone: this.state.phone,
            nationality: this.state.nationality,
        }]);

        this.notification.add("Student created", {
            type: "success",
        });

        this.state.name = "";
        this.state.phone = "";
        this.state.nationality= "",

        await this.loadStudents();
    }
}

StudentDashboard.template = "owl_practice.StudentDashboard";

registry.category("actions").add(
    "owl_practice.student_dashboard",
    StudentDashboard
);