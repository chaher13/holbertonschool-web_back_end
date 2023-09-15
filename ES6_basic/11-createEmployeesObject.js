export default function createEmployeesObject(departmentName, employees) {
  const MyObj = {
    [departmentName]: employees,
  };
  return MyObj;
}
