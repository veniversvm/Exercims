import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;


class AppointmentScheduler {

    DateTimeFormatter datePrinter = DateTimeFormatter.ofPattern("EEEE, MMMM d, yyyy");
    DateTimeFormatter hourPrinter = DateTimeFormatter.ofPattern("h:mm a");
    
    
    public LocalDateTime schedule(String appointmentDateDescription) {
        String[] appointmentArr = appointmentDateDescription.substring(0,10).split("/");
        String appointmentFormated = appointmentArr[2] +"-"+ appointmentArr[0] +"-"+ appointmentArr[1];
        return LocalDateTime.parse(appointmentFormated + "T" + appointmentDateDescription.substring(11));
    }

    public boolean hasPassed(LocalDateTime appointmentDate) {
        return appointmentDate.isBefore(LocalDateTime.now());
    }

    public boolean isAfternoonAppointment(LocalDateTime appointmentDate) {
        return appointmentDate.getHour() < 18 && appointmentDate.getHour() >= 12;
    }

    public String getDescription(LocalDateTime appointmentDate) {
        return "You have an appointment on " + datePrinter.format(appointmentDate) + ", at " + hourPrinter.format(appointmentDate) + ".";
    }

    public LocalDate getAnniversaryDate() {
        return LocalDate.of( LocalDateTime.now().getYear(), 9 , 15);
    }
}  