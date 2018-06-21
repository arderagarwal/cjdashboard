from django.shortcuts import render
from django.views.generic import ListView,DetailView
from recruiter.forms import UserForm,RecruiterForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from recruitertests.forms import TestForm as rforms
from recruitertests.models import Test
from recruiter.serializers import TechnologyVerticalSerializer,TrackSerializer,ContestSerializer,RecruiterSerializer,UserLevelSerializer,AssignmentSerializer,TestAssignSerializer,DetailedReportSerializer
from recruiter.models import Recruiter,UserLevel,Track,Contest,TechnologyVertical,Assignment,TestAssign,DetailedReport
from rest_framework.decorators import api_view
from rest_framework.response import Response
User = get_user_model()
class RecruiterListView(ListView):
 model = Recruiter
 context_object_name = 'recruit'
class RecruiterDetailView(DetailView):
 model = Recruiter
 context_object_name = 'recruiter'
 template_name = 'recruiter/dashboard.html'
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'recruiter/dashboard.html',{})
    else:
        return render(request, 'recruiter/login.html')
def assignment(request):
    if request.user.is_authenticated:
        technov = TechnologyVertical.objects.all()
        track = Track.objects.all()
        userlevel = UserLevel.objects.all()
        assign = Assignment.objects.all()
        return render(request, 'recruiter/assignments2.html',{'technov':technov,'track':track,'userlevel':userlevel,'assign':assign})
    else:
        return render(request, 'recruiter/login.html')
def createtest(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            test_form = rforms(data=request.POST)
            user = request.user

            if test_form.is_valid() :
                rtest = test_form.save()
                rtest.recruiter = request.user
                test_form.save()

            else:
                print(test_form.errors,)
        else:
            test_form = rforms()


        return render(request,'recruiter/createtest.html',
        {'test_form':test_form,
        })
    else:
        return render(request, 'recruiter/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        recruiter_form = RecruiterForm(data=request.POST)

        if user_form.is_valid() and recruiter_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            recruiter = recruiter_form.save(commit=False)
            recruiter.user = user

            recruiter.save()
            registered = True

        else:
            print(user_form.errors,recruiter_form.errors)
    else:
        user_form = UserForm()
        recruiter_form = RecruiterForm()

    return render(request,'recruiter/index.html',
    {'user_form':user_form,
    'recruiter_form':recruiter_form,
    'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("Account not active")
        else:
            print("someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,"recruiter/login.html",{})

@api_view(['GET', 'POST'])
def recruiter_list(request):

    if request.method == 'GET':
        recruiters = Recruiter.objects.all()
        serializer = RecruiterSerializer(recruiters, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecruiterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def recruiter_detail(request, pk):

    try:
        recruiter = Recruiter.objects.get(pk=pk)
    except Recruiter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecruiterSerializer(recruiter)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecruiterSerializer(recruiter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recruiter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'POST'])
def userlevel_list(request):

    if request.method == 'GET':
        userlevels = UserLevel.objects.all()
        serializer = UserLevelSerializer(userlevels, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserLevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def userlevel_detail(request, pk):

    try:
        userlevel = UserLevel.objects.get(pk=pk)
    except UserLevel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserLevelSerializer(userlevel)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserLevelSerializer(userlevel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userlevel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def technologyvertical_list(request):

    if request.method == 'GET':
        technologyverticals = TechnologyVertical.objects.all()
        serializer = TechnologyVerticalSerializer(technologyverticals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TechnologyVerticalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def technologyvertical_detail(request, pk):

    try:
        technologyvertical = TechnologyVertical.objects.get(pk=pk)
    except TechnologyVertical.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TechnologyVerticalSerializer(technologyvertical)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TechnologyVerticalSerializer(technologyvertical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        technologyvertical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def track_list(request):

    if request.method == 'GET':
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def track_detail(request, pk):

    try:
        track = Track.objects.get(pk=pk)
    except Track.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrackSerializer(track)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def contest_list(request):

    if request.method == 'GET':
        contests = Contest.objects.all()
        serializer = ContestSerializer(contests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def contest_detail(request, pk):

    try:
        contest = Contest.objects.get(pk=pk)
    except Contest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContestSerializer(contest)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContestSerializer(contest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def assignment_list(request):

    if request.method == 'GET':
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def assignment_detail(request, pk):

    try:
        assignment = Assignment.objects.get(pk=pk)
    except Assignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def testassign_list(request):

    if request.method == 'GET':
        testassigns = TestAssign.objects.all()
        serializer = TestAssignSerializer(testassigns, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TestAssignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def testassign_detail(request, pk):

    try:
        testassign = TestAssign.objects.get(pk=pk)
    except TestAssign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TestAssignSerializer(testassign)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TestAssignSerializer(testassign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        testassign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def detailedreport_list(request):

    if request.method == 'GET':
        detailedreports = DetailedReport.objects.all()
        serializer = DetailedReportSerializer(detailedreports, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DetailedReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def detailedreport_detail(request, pk):

    try:
        detailedreport = DetailedReport.objects.get(pk=pk)
    except DetailedReport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DetailedReportSerializer(detailedreport)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DetailedReportSerializer(detailedreport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        detailedreport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
