class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.professors = []  # Professor object
    def add_prof_tocourse(self, prof):
        if isinstance(prof, Professor):
            self.professors.append(prof)
        else: raise Exception(f'{prof} is not a propper Professor')
    def availabel_prof(self):
        for x in self.professors:
            print(x.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.reviews = []  # List of Review objects
        self.final_rating = None

    def add_review(self, review):
        self.reviews.append(review)
        self.final_rating = self.calculate_frating()
    def calculate_frating(self):
        total = 0
        cnt = 0
        for x in self.reviews:
            total += x.final_value
            cnt += 1
        return total/cnt

class Review:
    def __init__(self, review_text, like_dislike):
        self.upvotes = 0
        self.downvotes = 0
        self.review_text = review_text
        self.like_dislike = like_dislike  # True for like, False for dislike
        self.final_value = 0
        

    def calculate_final_value(self):
        if self.like_dislike == True:
            if self.downvotes == 0:
                return 5
            final_rating = 5 * (self.upvotes/(self.downvotes+self.upvotes))
        else:
            if self.upvotes == 0 and self.downvotes == 0:
                return 0
            final_rating = 5 * (self.downvotes/(self.downvotes+self.upvotes))
        return final_rating
    def apply_fvalue(self):
        self.final_value = self.calculate_final_value()

class Student:
    def __init__(self, name):
        self.name = name
        self.courses_taken = []  # List of Course objects

    def take_course(self, course):
        if isinstance(course, Course):
            self.courses_taken.append(course)
        else: raise Exception(f"{course} is not a propper Course")

    def student_add_review(self, course_name, review_text, like_dislike):
        if course_name not in [course.course_name for course in self.courses_taken]:
            raise Exception(f"{self.name} has not taken {course_name} yet.")
        
        course = next((course for course in self.courses_taken if course.course_name == course_name), None)
        if course is None:
            raise Exception(f"{course_name} does not exist.")
        
        review = Review(review_text, like_dislike)
        for professor in course.professors: #tofix
            professor.add_review(review)
        return review
    def student_vote(self, review, up):
        if isinstance(review, Review):
            if up == True:
                review.upvotes += 1
            else:
                review.downvotes += 1
            review.apply_fvalue()

import random
def main():
    # Create some professors
    prof1 = Professor("Professor 1")
    prof2 = Professor("Professor 2")

    # Create some courses and add professors to them
    course1 = Course("Course 1")
    course1.add_prof_tocourse(prof1)
    course2 = Course("Course 2")
    course2.add_prof_tocourse(prof2)

    # Create multiple students and have them take some courses
    students = [Student(f"Student {i}") for i in range(1, 6)]
    for student in students:
        student.take_course(course1)
        student.take_course(course2)

    # Have the students add reviews for the courses they've taken
    reviews = []
    for i, student in enumerate(students):
        review1 = student.student_add_review("Course 1", f"This course was great!", True)
        review2 = student.student_add_review("Course 2", f"This course was not so great.", False)
        reviews.append(review1)
        reviews.append(review2)

    # Students vote on the reviews
    for student in students:
        for review in reviews:
            vote = random.choice([True, False])  # Randomly assign True or False
            student.student_vote(review, vote)

    # Print out the reviews for each professor
    for prof in [prof1, prof2]:
        print(f"Reviews for {prof.name}:")
        for review in prof.reviews:
            print(f"Review text: {review.review_text}")
            print(f"Did the student like the course? {'Yes' if review.like_dislike else 'No'}")
            print(f"Final review value: {review.final_value}")

    # Print out the final rating for each professor
    for prof in [prof1, prof2]:
        print(f"Final rating for {prof.name}: {prof.calculate_frating()}")

    # Print out the available professors for each course
    for course in [course1, course2]:
        print(f"Available professors for {course.course_name}:")
        course.availabel_prof()

if __name__ == "__main__":
    main()

