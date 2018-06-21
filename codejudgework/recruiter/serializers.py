from rest_framework import serializers
from recruiter.models import Recruiter,UserLevel,Track,Contest,TechnologyVertical,Assignment,TestAssign,DetailedReport

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'


class UserLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLevel
        fields = ('Name','Level')


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('name',)

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = ('name','track_id')

class TechnologyVerticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyVertical
        fields = ('name',)

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('name','track_id','vertical_id','tags','description')

class TestAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAssign
        fields = ('contest_id','assignment_id','language','user_id','user_email','test_link','status','language_allowed')

class DetailedReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailedReport
        fields = ('sonar_project_id','s3s3_bucket_path','language','test_id')
