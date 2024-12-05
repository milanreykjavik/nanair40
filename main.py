from baseClasses.WorkOrder import WorkOrder
from logic.workOrderHandler import WorkOrderHandler
from baseClasses.WorkReport import WorkReport
from logic.workReportHandler import WorkReportHandler

x = WorkOrderHandler()
y = WorkReportHandler()

wo = WorkOrder(45, "2024", "desc", 1, 1, 1, 1, True)
print(wo)

rep = WorkReport(1, 45, "test", "2024", 10, "com")
print(rep)


print(x.addWorkOrder(wo))
print(x.listWorkOrders())

print(y.addWorkReport(rep))
print(y.listWorkReports())
