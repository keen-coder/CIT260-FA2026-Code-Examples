from types import MappingProxyType

class Course:
    """
    Represents an immutable college course.

    Once created, a Course object's state cannot be modified.
    Mutable collections are converted to immutable equivalents
    to prevent accidental changes.
    """

    def __init__(self, course_number: int, credits: float, name: str,
        prerequisites: list[str], degree_programs: set[str], 
        grade_weights: dict[str, float]
    ):
        """
        Initializes a Course object.

        Args:
            course_number: The course number.
            credits: The number of credit hours.
            name: The course name.
            prerequisites: A list of prerequisite courses.
            degree_programs: Degree programs requiring the course.
            grade_weights: Categories and their grading weights.
        """

        self.__course_number = course_number
        self.__credits = credits
        self.__name = name

        # Convert mutable collections to immutable forms.
        self.__prerequisites = tuple(prerequisites)
        self.__degree_programs = frozenset(degree_programs)
        self.__grade_weights = MappingProxyType(dict(grade_weights))

    def get_course_number(self) -> int:
        """
        Returns the course number.

        Returns:
            The course number.
        """
        return self.__course_number

    def get_credits(self) -> float:
        """
        Returns the number of credit hours.

        Returns:
            The course's credit value.
        """
        return self.__credits

    def get_name(self) -> str:
        """
        Returns the course name.

        Returns:
            The course name.
        """
        return self.__name

    def get_prerequisites(self) -> tuple[str, ...\]:
        """
        Returns the prerequisite courses.

        Returns:
            A tuple containing prerequisite course numbers.
        """
        return self.__prerequisites

    def get_degree_programs(self) -> frozenset[str\]:
        """
        Returns the degree programs that require this course.

        Returns:
            A frozenset of degree program names.
        """
        return self.__degree_programs

    def get_grade_weights(self):
        """
        ng categories and weights.

        Returns:
            A read-only dictionary containing grading weights.
        """
        return self.__grade_weights

    def __str__(self) -> str:
        """
        Returns a string representation of the course.

        Returns:
            A formatted string describing the course.
        """
        return (
            f'{self.__course_number} - '
            f'{self.__name} '
            f'({self.__credits} Credits)'
        )