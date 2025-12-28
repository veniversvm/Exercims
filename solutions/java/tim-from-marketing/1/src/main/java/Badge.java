class Badge {

    public String print(Integer id, String name, String department) {
        String isID = id == null ? "" : "["+  id + "] - ";
        String isDepartment = department == null ? " - OWNER" : " - " + department.toUpperCase();
        return isID + name + isDepartment;
    }
}
