# StudyTimeCalculator.py

# Жилд хичээллэх долоо хоногийн тоо
WEEKS_IN_YEAR = 39

# Сонирхсон хичээл үзэх долоо хоногийн цаг
INTEREST_HOURS_PER_WEEK = 4

# 1978-1988 онд долоо хоногт хичээллэх өдөр
WORK_DAYS_PER_WEEK_OLD = 6

# 2006-2018 онд долоо хоногт хичээллэх өдөр
WORK_DAYS_PER_WEEK_NEW = 5

# Дадлагын нийт долоо хоног
INTERNSHIP_WEEKS = 8

# Дадлагын өдөрт хичээллэх цаг
INTERNSHIP_HOURS_PER_DAY = 8


def calculatePrimaryHours1978_1988():
    """
    1978-1988 оны дунд сургуульд суралцах нийт цагийг тооцох функц.
    """
    # 1-3 анги: 7 хоногт 4 цаг хичээллэх, 6 өдөр, жилд 39 долоо хоног, нийт 3 жил
    hours1_3 = 4 * WORK_DAYS_PER_WEEK_OLD * WEEKS_IN_YEAR * 3

    # 4-8 анги: 7 хоногт нийт 34 цагийн хичээл, жилд 39 долоо хоног, нийт 5 жил
    hours4_8 = 34 * WEEKS_IN_YEAR * 5

    # 9-10 анги: 7 хоногт 6 цаг хичээллэх, 6 өдөр, жилд 39 долоо хоног, нийт 2 жил
    hours9_10 = 6 * WORK_DAYS_PER_WEEK_OLD * WEEKS_IN_YEAR * 2

    return hours1_3 + hours4_8 + hours9_10  # Нийт суралцах цаг


def calculatePrimaryHours2006_2018():
    """
    2006-2018 оны дунд сургуульд суралцах нийт цагийг тооцох функц.
    """
    # 1-5 анги: 7 хоногт 4 цаг хичээллэх, 5 өдөр, жилд 39 долоо хоног, нийт 5 жил
    hours1_5 = 4 * WORK_DAYS_PER_WEEK_NEW * WEEKS_IN_YEAR * 5

    # 6-12 анги: 7 хоногт 6 цаг хичээллэх, 5 өдөр, жилд 39 долоо хоног, нийт 7 жил
    hours6_12 = 6 * WORK_DAYS_PER_WEEK_NEW * WEEKS_IN_YEAR * 7

    return hours1_5 + hours6_12  # Нийт суралцах цаг


def calculateUniversityHours(totalYears, workDaysPerWeek):
    """
    Дээд сургуульд суралцах нийт цагийг тооцох функц.
    
    :param totalYears: Тухайн хугацаанд хэдэн жил сурсан
    :param workDaysPerWeek: Хичээллэх өдөрт хэдэн өдөр ажилласан
    :return: Нийт суралцах цаг
    """
    # 7 хоногт 3 цаг хичээллэх, жилд 39 долоо хоног
    return totalYears * (3 * workDaysPerWeek * WEEKS_IN_YEAR)


def calculateInterestHours(totalYears):
    """
    Сонирхсон хичээлд зарцуулсан нийт цагийг тооцох функц.
    
    :param totalYears: Тухайн хугацаанд хэдэн жил суралцсан
    :return: Нийт зарцуулсан цаг
    """
    return INTEREST_HOURS_PER_WEEK * WEEKS_IN_YEAR * totalYears


def calculateInternshipPercentage(totalWeeks):
    """
    Үйлдвэрлэлийн дадлагын эзлэх хувийг тооцох функц.
    
    :param totalWeeks: Нийт долоо хоног
    :return: Эзлэх хувь (%)
    """
    # 8 долоо хоногийн дадлага, долоо хоногт 5 өдөр, өдөрт 8 цаг
    internship_hours = INTERNSHIP_WEEKS * WORK_DAYS_PER_WEEK_NEW * INTERNSHIP_HOURS_PER_DAY
    total_hours = totalWeeks * WORK_DAYS_PER_WEEK_NEW * 8  # Нийт цагийн тоо

    return (internship_hours / total_hours) * 100


def main():
    # 1978-1988 оны дунд сургууль
    primaryHours1978_1988 = calculatePrimaryHours1978_1988()
    
    # 1988-1993 оны дээд сургууль
    universityHours1988_1993 = calculateUniversityHours(5, WORK_DAYS_PER_WEEK_OLD)
    
    # 2006-2018 оны дунд сургууль
    primaryHours2006_2018 = calculatePrimaryHours2006_2018()
    
    # 2018-2022 оны дээд сургууль
    universityHours2018_2022 = calculateUniversityHours(4, WORK_DAYS_PER_WEEK_NEW)
    
    # Сонирхсон хичээлд зарцуулсан цагууд
    interestHours1978_1988 = calculateInterestHours(10)
    interestHours1988_1993 = calculateInterestHours(5)
    interestHours2006_2018 = calculateInterestHours(12)
    interestHours2018_2022 = calculateInterestHours(4)
    
    # Үйлдвэрлэлийн дадлагын эзлэх хувийг тооцох
    internshipPercentage1988_1993 = calculateInternshipPercentage(195)  # 1978-1988 дунд + 1988-1993 дээд сургуульд суралцсан нийт 195 долоо хоног
    internshipPercentage2018_2022 = calculateInternshipPercentage(156)  # 2018-2022 дээд сургуульд суралцсан нийт 156 долоо хоног
    
    # Хамгийн их суралцах цагийг тодорхойлох
    maxStudyHours = max(primaryHours1978_1988, universityHours1988_1993,
                        primaryHours2006_2018, universityHours2018_2022)
    
    if maxStudyHours == primaryHours1978_1988:
        mostStudyPeriod = "1978-1988 дунд сургууль"
    elif maxStudyHours == universityHours1988_1993:
        mostStudyPeriod = "1988-1993 дээд сургууль"
    elif maxStudyHours == primaryHours2006_2018:
        mostStudyPeriod = "2006-2018 дунд сургууль"
    else:
        mostStudyPeriod = "2018-2022 дээд сургууль"
    
    # Хариуг хэвлэх хэсэг
    print(f"1978-1988 онд сурагч нийт суралцах цаг: {primaryHours1978_1988} цаг")
    print(f"1978-1988 онд сонирхсон хичээлд зарцуулсан цаг: {interestHours1978_1988} цаг")
    print(f"1988-1993 онд оюутан нийт суралцах цаг: {universityHours1988_1993} цаг")
    print(f"1988-1993 онд сонирхсон хичээлд зарцуулсан цаг: {interestHours1988_1993} цаг")
    print(f"1988-1993 онд үйлдвэрлэлийн дадлага нийт суралцах хугацаанд эзлэх хувь: {internshipPercentage1988_1993:.2f}%")
    print(f"2006-2018 онд сурагч нийт суралцах цаг: {primaryHours2006_2018} цаг")
    print(f"2006-2018 онд сонирхсон хичээлд зарцуулсан цаг: {interestHours2006_2018} цаг")
    print(f"2018-2022 онд оюутан нийт суралцах цаг: {universityHours2018_2022} цаг")
    print(f"2018-2022 онд сонирхсон хичээлд зарцуулсан цаг: {interestHours2018_2022} цаг")
    print(f"2018-2022 онд үйлдвэрлэлийн дадлага нийт суралцах хугацаанд эзлэх хувь: {internshipPercentage2018_2022:.2f}%")
    print(f"Хамгийн их цаг зарцуулан суралцсан нь: {mostStudyPeriod}")


if __name__ == "__main__":
    main()
1111111111111111111
