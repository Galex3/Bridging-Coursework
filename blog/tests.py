from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Post, CVExperience, HardSkill, SoftSkill, Project, Interest, Language, Education


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test', email='test@bham.ac.uk', password='top_secret')
        Post.objects.create(author=self.user, title="TestCase1", content="Content test 1")

    def test_post_creation(self):
        test1 = Post.objects.get(title="TestCase1")
        self.assertEqual(test1.status, 0)
        self.assertEqual(test1.content, 'Content test 1')
        self.assertEqual(test1.title, 'TestCase1')


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')


class CVModelTest(TestCase):

    def test_create_and_read_education(self):
        first_item = Education()
        first_item.degree = 'Test'
        first_item.institution = 'Inst Test'
        first_item.duration = '2020'
        first_item.item1 = 'Coursework 1'
        first_item.item1_grade = 99.99
        first_item.item2 = 'Coursework 2'
        first_item.item2_grade = 80
        first_item.item2 = 'Coursework 3'
        first_item.item2_grade = 45.44
        first_item.save()
        saved_items = Education.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertEqual(saved_items[0].institution, 'Inst Test')

    def test_create_and_read_experience(self):
        first_item = CVExperience()
        first_item.role = 'Test'
        first_item.company = 'Company'
        first_item.duration = '2020'
        first_item.item1 = 'Item 1'
        first_item.item2 = 'Item 2'
        first_item.item2 = 'Item 3'
        first_item.save()
        saved_items = CVExperience.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertEqual(saved_items[0].duration, '2020')

    def test_create_and_read_hard_skill(self):
        first_item = HardSkill(icon='fas fa-school')
        first_item.save()
        saved_items = HardSkill.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertEqual(saved_items[0].icon, 'fas fa-school')

    def test_create_and_read_soft_skill(self):
        first_item = SoftSkill()
        first_item.text = 'TDD Expert'
        first_item.save()
        saved_items = SoftSkill.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertEqual(saved_items[0].text, 'TDD Expert')

    def test_create_and_read_project(self):
        first_item = Project()
        first_item.title = 'Django App'
        first_item.description = 'Blog and CV'
        first_item.duration = 'June 2020'
        first_item.link = ''
        first_item.save()
        saved_items = Project.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertEqual(saved_items[0].description, 'Blog and CV')

    def test_create_and_read_interest(self):
        first_item = Interest(icon='fas fa-palette')
        first_item.save()
        saved_items = Interest.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertEqual(saved_items[0].icon, 'fas fa-palette')

    def test_create_and_read_language(self):
        first_item = Language()
        first_item.name = 'Arabic'
        first_item.proficiency = 'Noob'
        first_item.level = 1
        first_item.save()
        saved_items = Language.objects.all()
        self.assertEqual(saved_items.count(), 1)
        self.assertEqual(saved_items[0].proficiency, 'Noob')
