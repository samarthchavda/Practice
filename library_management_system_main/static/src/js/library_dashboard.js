import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class LibraryDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.action = useService("action");

        this.state = useState({
            total_books: 0,
            total_members: 0,
            total_issue_books: 0,
        });

        onWillStart(async () => {
            const data = await this.orm.searchRead("library.dashboard", [], [
                "total_books",
                "total_members",
                "total_issue_books",
                "total_fine_amount",
            ]);

            if (data.length) {
                Object.assign(this.state, data[0]);
            }
        });
    }

    openBooks(){
        this.action.doAction({
            type :"ir.actions.act_window",
            name :"Library Books",
            res_model :"lib.books.data",
            view_mode :"list,form",
            views : [[false,"list"],[false,"form"]],
            target : "current",
        })
    }

    openMember(){
        this.action.doAction({
            type :"ir.actions.act_window",
            name :"Library Members",
            res_model :"lib.member",
            view_mode : "list,form",
            views : [[false,"list"],[false,"form"]],
            target : "current"
        })
    }

    openIssue(){
        this.action.doAction({
            type:"ir.actions.act_window",
            name:"Books issue",
            res_model:"lib.issue",
            view_mode:"list,form",
            views:[[false,"list"],[false,"form"]],
            target:"current"
        })
    }

}

LibraryDashboard.template = "library_management_system_main.LibraryDashboard";

registry.category("actions").add("library_dashboard_action", LibraryDashboard);