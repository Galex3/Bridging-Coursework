from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .forms import CommentForm
from .models import Post, CVExperience, HardSkill, SoftSkill, Project, Interest, Language, Education


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-published_date')
    template_name = 'index.html'
    paginate_by = 3


class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'all_search_results'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('search_box').strip()
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-published_date')
        return object_list


def cv(request):
    if request.method == 'POST':
        # CVExperience.objects.create(role=request.POST['role_text'], company=request.POST['company_text'],
        #                            duration=request.POST['duration_text'], item1=request.POST['item1_text'],
        #                            item2=request.POST['item2_text'], item3=request.POST['item3_text'])
        # HardSkill.objects.create(icon=request.POST['hard_skill_text'])
        # SoftSkill.objects.create(text=request.POST['soft_skill_text'])
        # Project.objects.create(title=request.POST['title_text'], description=request.POST['description_text'],
        #                       duration=request.POST['duration_text'], link=request.POST['link_text'])
        # Interest.objects.create(icon=request.POST['icon_text'])
        # Language.objects.create(name=request.POST['name_text'], proficiency=request.POST['proficiency_text'],
        #                        level=request.POST['level_text'])
        # Education.objects.create(degree=request.POST['degree_text'], institution=request.POST['institution_text'],
        #                            duration=request.POST['duration_text'], item1=request.POST['item1_text'],
        #                            item1_grade=request.POST['item1_grade_text'], item2=request.POST['item2_text'],
        #                         item2_grade=request.POST['item2_grade_text'], item3=request.POST['item3_text'],
        #                         item3_grade=request.POST['item3_grade_text'])
        return redirect('/cv')

    exp = CVExperience.objects.all()
    hs = HardSkill.objects.all()
    ss = SoftSkill.objects.all()
    proj = Project.objects.all()
    inte = Interest.objects.all()
    lang = Language.objects.all()
    edu = Education.objects.all()
    return render(request, 'cv.html',
                  {'exp': exp, 'hs': hs, 'ss': ss, 'proj': proj, 'inte': inte, 'lang': lang, 'edu': edu})


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("created_date")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
