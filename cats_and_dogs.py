class CatYears:
    def __init__(self, age: int):
        self.age = age
        self.max_coefficient = 4
        self.ages = {1: 15, 2: 9, 3: self.max_coefficient}

    def calculate_age(self) -> list:
        return sum([self.ages.get(i, self.max_coefficient) for i in range(1, self.age + 1)])


class DogYears(CatYears):
    def __init__(self, age):
        super().__init__(age)
        self.max_coefficient = 5
        self.ages = {1: 15, 2: 9, 3: self.max_coefficient}


def human_years_cat_years_dog_years(age: int) -> list:
    if not age:
        raise ValueError('Incorrect age')

    cat_years = CatYears(age).calculate_age()
    dog_years = DogYears(age).calculate_age()

    return [age, cat_years, dog_years]


if __name__ == '__main__':
    assert human_years_cat_years_dog_years(1) == [1, 15, 15]
    assert human_years_cat_years_dog_years(2) == [2, 24, 24]
    assert human_years_cat_years_dog_years(10) == [10, 56, 64]
    assert human_years_cat_years_dog_years(0) == []
