from ui.baseUI import BaseUI
from baseClasses.Work import WorkOrder  
from baseClasses.Work import WorkReport
import os

class JanitorUI(BaseUI):
    def __init__(self):
        
        # Im just using sample data that i made for now :)
        
        workOrderclass = WorkOrder()
        self.work_orders = [ # these are just placeholders for now
            WorkOrder(id=1, date="2024-12-04", description="Fix lights", propertyNumber=11, userID=1, priority=1),
            WorkOrder(id=2, date="2024-12-03", description="Repair roof", propertyNumber=32, userID=2, priority=0),
        ]

        workReportclass = WorkReport()
        self.work_reports = [ # these are just placeholders for now
            WorkReport(id=55, description="Fixed the lights", date="2024-12-03", cost=1000, comment="Chuck Norris"),
            WorkReport(id=89, description="Built a house", date="2024-12-11", cost=5000, comment="Bob"),
        ]

    def workOrders(self):
        """Displays the work orders using WorkOrder objects."""
        while True:
            clearTerminal()
            wo_header = "+-----------------------+----------------+------------------+--------------+\n"+(" ")*7
            wo_header += "| Work                  | Location       | How important    | Identifier   |\n"+(" ")*7
            wo_header += "+-----------------------+----------------+------------------+--------------+" # combining to make a uniqe header for this UI
            table_rows = "\n".join((" ")*7+f"| {order.description:<21} | Property {order.propertyNumber:<5} | {order.priority:<16} | {order.id:<12} |" for order in self.work_orders) # a for loop to create a table from the work orders
            wo_footer = (" ")*7+"+-----------------------+----------------+------------------+--------------+"

            menu_content = f"{wo_header}\n{table_rows}\n{wo_footer}" # combine everything above into one table

            self.printBaseMenu("Work Orders",[menu_content],"Enter work order ID")
            work_id, is_valid = self.takeInput(["[B]ack", "[Q]uit"]) #only having 2 options right now, will add one for id
    

            

            if is_valid:
                if work_id.lower() == 'q':
                    return 'q' # quits the whole program
                elif work_id.lower() == 'b':
                    return False # returns to the previous page

    def workReports(self):
        """Displays the work reports using WorkReport objects."""
        while True:
            clearTerminal()
            wr_header = "+---------------------------------+-------------------------+-------------+\n"+(" ")*7
            wr_header += "| TASK                            | PERSON                  | ID          |\n"+(" ")*7
            wr_header += "+---------------------------------+-------------------------+-------------+" # creating a header for this ui
            wr_rows = "\n".join((" ")*7+f"| {report.description:<31} | {report.comment:<23} | {report.id:<11} |" for report in self.work_reports) # a for loop to add all of the reports
            wr_footer = (" ")*7+"+---------------------------------+-------------------------+-------------+"

            menu_content = f"{wr_header}\n{wr_rows}\n{wr_footer}" # combine everything into one

            self.printBaseMenu("Work Reports",[menu_content],"Choose a ID to create a work report on") 
            report_id, is_valid = self.takeInput(["[B]ack", "[Q]uit"])
            

            if is_valid:
                if report_id.lower() == 'b':
                    return False # returns to the previous page
                elif report_id.lower() == 'q':
                    return "q" # quits the whole program

def clearTerminal():
    """Clear the terminal screen before a new menu is printed"""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')