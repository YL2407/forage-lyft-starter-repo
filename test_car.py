from car_factory import CarFactory
from datetime import date

carFactory = CarFactory()
def test():
    count = 1
    try:
        assert carFactory.create_calliope(date.today(), date.today(), 70000, 50000).needs_service() == False
        count+=1
        assert carFactory.create_glissade(date.today(), date(2020,1,1), 70000, 50000).needs_service() == True
        count+=1
        assert carFactory.create_palindrome(date.today(), date.today(), True).needs_service() == True
        count+=1
        assert carFactory.create_palindrome(date.today(), date.today(), False).needs_service() == False
        count+=1
        assert carFactory.create_rorschach(date.today(), date.today(), 70000, 10000).needs_service() == True
        count+=1
        assert carFactory.create_thovex(date.today(), date(2016,1,1), 70000, 70000).needs_service() == True
        count+=1
        return count
    except:
        return count


if __name__ == "__main__":
    if test() == 7:
        print("Everything passed")
    else:
        print("Failed test " + str(test()))
