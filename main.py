import django_setup

from lesson1.models import User, Category, Product, Student, Course, MyModel

#user = User.objects.filter(id=1).last()
#print(user)
#print(user[0].email)


#user = User.objects.filter(id=4).all()
#print(user)

#not_needed_user = User.objects.get(id=2)
#not_needed_user.delete()

#user_to_update = User.objects.get(id = 1)
#user_to_update.name = "Антон"
#user_to_update.email = "anton@gmail.com"
#user_to_update.bio = "kiwefhwuefhwefhuweufhwefhuhu"
#user_to_update.save()

#users = User.objects.all()
#for u in users:
    #print(u.email)


# category1 = Category(name = "Dairy products")
# category1.save()
#
# new_product = Product(
#     name = "Milk",
#     price = 22.5,
#     description = "",
#     category = category1
# ).save()


# product = Product.objects.filter(id=1).first()
# print(product.name)
# print(product.category.name)
#
# category = Category.objects.get(id=2)
# print(category.products)

#Student(name = "Dsq").save()

# Course(title = "Some Course1").save()
# Course(title = "Some Course2").save()

# student1 = Student.objects.get(id=2)
# course1 = Course.objects.get(id=1)
# student1.courses.add(course1)
#
# print(course1.student_set.all())




