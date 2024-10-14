package biydaalt;
public class StudyTimeCalculator {

    private static final int WEEKS_IN_YEAR = 39; // Жилд хичээллэх долоо хоногийн тоо
    private static final int INTEREST_HOURS_PER_WEEK = 4; // Сонирхсон хичээл үзэх 7 хоногийн цаг
    private static final int WORK_DAYS_PER_WEEK_OLD = 6; // 1978-1988 онд долоо хоногт хичээллэх өдөр
    private static final int WORK_DAYS_PER_WEEK_NEW = 5; // 2006-2018 онд долоо хоногт хичээллэх өдөр
    private static final int INTERNSHIP_WEEKS = 8; // Дадлагын нийт долоо хоног
    private static final int INTERNSHIP_HOURS_PER_DAY = 8; // Дадлагын өдөрт хичээллэх цаг

    public static void main(String[] args) {
    	int primaryHours1978_1988 = calculatePrimaryHours1978_1988();
		int universityHours1988_1993 = calculateUniversityHours(5, WORK_DAYS_PER_WEEK_OLD);        
        int primaryHours2006_2018 = calculatePrimaryHours2006_2018();        
        int universityHours2018_2022 = calculateUniversityHours(4, WORK_DAYS_PER_WEEK_NEW);
        
        // Сонирхсон хичээлд зарцуулсан цагууд
        int interestHours1978_1988 = calculateInterestHours(10);
        int interestHours1988_1993 = calculateInterestHours(5);
        int interestHours2006_2018 = calculateInterestHours(12);
        int interestHours2018_2022 = calculateInterestHours(4);
        
        // Үйлдвэрлэлийн дадлагын эзлэх хувийг тооцох
        double internshipPercentage1988_1993 = calculateInternshipPercentage(195); // 1978-1988 дунд + 1988-1993 дээд сургуульд суралцсан нийт 7 хоног
        double internshipPercentage2018_2022 = calculateInternshipPercentage(156); // 2018-2022 дээд сургуульд суралцсан нийт 7 хоног

        // Хамгийн их суралцах цагийг тодорхойлох
        int maxStudyHours = Math.max(Math.max(primaryHours1978_1988, universityHours1988_1993),
                                     Math.max(primaryHours2006_2018, universityHours2018_2022));
        String mostStudyPeriod;
        if (maxStudyHours == primaryHours1978_1988) {
            mostStudyPeriod = "1978-1988 дунд сургууль";
        } else if (maxStudyHours == universityHours1988_1993) {
            mostStudyPeriod = "1988-1993 дээд сургууль";
        } else if (maxStudyHours == primaryHours2006_2018) {
            mostStudyPeriod = "2006-2018 дунд сургууль";
        } else {
            mostStudyPeriod = "2018-2022 дээд сургууль";
        }

        // Хариуг хэвлэх хэсэг
        System.out.println("1978-1988 онд сурагч нийт суралцах цаг: " + primaryHours1978_1988 + " цаг");
        System.out.println("1978-1988 онд сонирхсон хичээлд зарцуулсан цаг: " + interestHours1978_1988 + " цаг");
        System.out.println("1988-1993 онд оюутан нийт суралцах цаг: " + universityHours1988_1993 + " цаг");
        System.out.println("1988-1993 онд сонирхсон хичээлд зарцуулсан цаг: " + interestHours1988_1993 + " цаг");
        System.out.println("1988-1993 онд үйлдвэрлэлийн дадлага нийт суралцах хугацаанд эзлэх хувь: " + internshipPercentage1988_1993 + "%");
        System.out.println("2006-2018 онд сурагч нийт суралцах цаг: " + primaryHours2006_2018 + " цаг");
        System.out.println("2006-2018 онд сонирхсон хичээлд зарцуулсан цаг: " + interestHours2006_2018 + " цаг");
        System.out.println("2018-2022 онд оюутан нийт суралцах цаг: " + universityHours2018_2022 + " цаг");
        System.out.println("2018-2022 онд сонирхсон хичээлд зарцуулсан цаг: " + interestHours2018_2022 + " цаг");
        System.out.println("2018-2022 онд үйлдвэрлэлийн дадлага нийт суралцах хугацаанд эзлэх хувь: " + internshipPercentage2018_2022 + "%");
        System.out.println("Хамгийн их цаг зарцуулан суралцсан нь: " + mostStudyPeriod);
    }

    private static int calculatePrimaryHours1978_1988() {
    	// 1-3 анги: 7 хоногт 4 цаг хичээллэх 6 өдөр, жилд 39 долоо хоног, нийт 3 жил
        int hours1_3 = 4 * WORK_DAYS_PER_WEEK_OLD * WEEKS_IN_YEAR * 3;
        // 4-8 анги: 7 хоногт нийт 34 цагийн хичээл, жилд 39 долоо хоног, нийт 5 жил
        int hours4_8 = 34 * WEEKS_IN_YEAR * 5;
        // 9-10 анги: 7 хоногт 6 цаг хичээллэх 6 өдөр, жилд 39 долоо хоног, нийт 2 жил
        int hours9_10 = 6 * WORK_DAYS_PER_WEEK_OLD * WEEKS_IN_YEAR * 2;
        return hours1_3 + hours4_8 + hours9_10; // Нийт суралцах цаг
	}

	private static int calculatePrimaryHours2006_2018() {
		// 1-5 анги: 7 хоногт 4 цаг хичээллэх 5 өдөр, жилд 39 долоо хоног, нийт 5 жил
        int hours1_5 = 4 * WORK_DAYS_PER_WEEK_NEW * WEEKS_IN_YEAR * 5;
        // 6-12 анги: 7 хоногт 6 цаг хичээллэх 5 өдөр, жилд 39 долоо хоног, нийт 7 жил
        int hours6_12 = 6 * WORK_DAYS_PER_WEEK_NEW * WEEKS_IN_YEAR * 7;
        return hours1_5 + hours6_12; // Нийт суралцах цаг
	}

	private static int calculateUniversityHours(int totalYears, int workDaysPerWeek) {
        // 7 хоногт 3 цаг хичээллэх, жилд 39 долоо хоног
        return totalYears * (3 * workDaysPerWeek * WEEKS_IN_YEAR);
    }

	// Сонирхсон хичээлд зарцуулсан цагийг бодох функц
    private static int calculateInterestHours(int totalYears) {
        return INTEREST_HOURS_PER_WEEK * WEEKS_IN_YEAR * totalYears;
    }

    // Үйлдвэрлэлийн дадлагын эзлэх хувийг тооцох функц
    private static double calculateInternshipPercentage(int totalWeeks) {
        // 8 долоо хоногийн дадлага, долоо хоногт 5 өдөр, өдөрт 8 цаг
        int internshipHours = INTERNSHIP_WEEKS * WORK_DAYS_PER_WEEK_NEW * INTERNSHIP_HOURS_PER_DAY;
        // Хувь бодох
        return ((double) internshipHours / (totalWeeks * WORK_DAYS_PER_WEEK_NEW * 8)) * 100;
    }
}
