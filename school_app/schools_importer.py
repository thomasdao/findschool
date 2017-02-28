import csv, os
from school_app.models import School, Course

def add_schools():
    path = os.path.join(os.path.dirname(__file__), "schools.csv")
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['Name of institution']

            # Check if name exists
            school = None
            try:
                school = School.objects.filter(name=name)[0]
            except:
                school = School()
                school.name = name
                school.school_type = row['Type of institution']
                school.level = row['Level']
                school.country = row['Country']
                school.country_code = get_country_code(school.country)
                school.state = row['State/Province']
                school.city = row['City']
                school.website = row['Website']
                school.save()

            # Add Course
            course = None
            area_of_study = row['Area of study']
            programme = row['Programme']
            try:
                course = Course.objects.filter(
                    area_of_study=area_of_study,
                    programme=programme)[0]
            except:
                course = Course()
                course.school = school
                course.area_of_study = area_of_study
                course.programme = programme
                course.save()

def get_country_code(country):
    if country == "Australia":
        return "au"

    if "USA" in country:
        return "us"

    if country == "Canada":
        return "ca"

    if country == "England":
        return "uk"
