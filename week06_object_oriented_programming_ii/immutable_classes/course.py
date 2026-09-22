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

        # Convert mutable collections to immutable forms
        self.__prerequisites = tuple(prerequisites)
        self.__degree_programs = frozenset(degree_programs)
        self.__grade_weights = MappingProxyType(grade_weights)

    def get_course_number(self) -> int:
        return self.__course_number

    def get_credits(self) -> float:
        return self.__credits

    def get_name(self) -> str:
        return self.__name

    def get_prerequisites(self) -> tuple[str]:
        return self.__prerequisites

    def get_degree_programs(self) -> frozenset[str]:
        return self.__degree_programs

    def get_grade_weights(self) -> MappingProxyType[str, float]:
        return self.__grade_weights