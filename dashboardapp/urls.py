from django.urls import path
from. import views

urlpatterns = [
     path('test/',views.test,name='test'),
     path('base/',views.base,name='base'),
     path('register/',views.registeruser,name='register'),
     path('register/',views.registeruser,name='register'),
     path('login/',views.loginuser,name='login'),
     path('logout/',views.logoutuser,name='logout'),
     path('student/',views.tablestudent,name='student'),
     path('profile/',views.user_profile,name='profile'),
     path('cprofile/',views.createprofile,name='cprofile'),
     path('updateprofile/<str:pk>',views.updateprofile,name='updateprofile'),
     path('',views.mainpage,name='index'),

     path('mentor_table/',views.mentortable,name='mentor-t'),
     #students
     #1
     path('student_1A_table',views.student_1A_table,name='student-1A-t'),
     path('student_1B_table',views.student_1B_table,name='student-1B-t'),
     path('student_1D_table',views.student_1D_table,name='student-1D-t'),
     path('student_1F_table',views.student_1F_table,name='student-1F-t'),
     #2
     path('student_2A_table',views.student_2A_table,name='student-2A-t'),
     path('student_2B_table',views.student_2B_table,name='student-2B-t'),
     path('student_2D_table',views.student_2D_table,name='student-2D-t'),
     path('student_2F_table',views.student_2F_table,name='student-2F-t'),
     #3
     path('student_3A_table',views.student_3A_table,name='student-3A-t'),
     path('student_3B_table',views.student_3B_table,name='student-3B-t'),
     path('student_3D_table',views.student_3D_table,name='student-3D-t'),
     path('student_3F_table',views.student_3F_table,name='student-3F-t'),
     
     #4   
     path('student_4A_table',views.student_4A_table,name='student-4A-t'),
     path('student_4B_table',views.student_4B_table,name='student-4B-t'),
     path('student_4D_table',views.student_4D_table,name='student-4D-t'),
     path('student_4F_table',views.student_4F_table,name='student-4F-t'),
     #5
     path('student_5A_table',views.student_5A_table,name='student-5A-t'),
     path('student_5B_table',views.student_5B_table,name='student-5B-t'),
     path('student_5D_table',views.student_5D_table,name='student-5D-t'),
     path('student_5F_table',views.student_5F_table,name='student-5F-t'),
     #6
     path('student_6A_table',views.student_6A_table,name='student-6A-t'),
     path('student_6B_table',views.student_6B_table,name='student-6B-t'),
     path('student_6D_table',views.student_6D_table,name='student-6D-t'),
     path('student_6F_table',views.student_6F_table,name='student-6F-t'),
     
     #7
     path('student_7A_table',views.student_7A_table,name='student-7A-t'),
     path('student_7B_table',views.student_7B_table,name='student-7B-t'),
     path('student_7D_table',views.student_7D_table,name='student-7D-t'),
     path('student_7F_table',views.student_7F_table,name='student-7F-t'),
     #8
     path('student_8A_table',views.student_8A_table,name='student-8A-t'),
     path('student_8B_table',views.student_8B_table,name='student-8B-t'),
     path('student_8D_table',views.student_8D_table,name='student-8D-t'),
     path('student_8F_table',views.student_8F_table,name='student-8F-t'),
     #9
     path('student_9A_table',views.student_9A_table,name='student-9A-t'),
     path('student_9B_table',views.student_9B_table,name='student-9B-t'),
     path('student_9D_table',views.student_9D_table,name='student-9D-t'),
     path('student_9F_table',views.student_9F_table,name='student-9F-t'),
     
     #10
     path('student_10A_table',views.student_10A_table,name='student-10A-t'),
     path('student_10B_table',views.student_10B_table,name='student-10B-t'),
     path('student_10D_table',views.student_10D_table,name='student-10D-t'),
     
     #11
     path('student_11A_table',views.student_11A_table,name='student-11A-t'),
     path('student_11B_table',views.student_11B_table,name='student-11B-t'),
     path('student_11D_table',views.student_11D_table,name='student-11D-t'),
     
     #createform
     path('createstudent',views.createeforms,name='createstudent'),
     path('create1a',views.createe1a,name='create1a'),
     path('create1b',views.createe1b,name='create1b'),
     path('create1d',views.createe1d,name='create1d'),
     path('create1f',views.createe1f,name='create1f'),
     path('create2a',views.createe2a,name='create2a'),
     path('create2b',views.createe2b,name='create2b'),
     path('create2d',views.createe2d,name='create2d'),
     path('create2f',views.createe2f,name='create2f'),
     path('create3a',views.createe3a,name='create3a'),
     path('create3b',views.createe3b,name='create3b'),
     path('create3d',views.createe3d,name='create3d'),
     path('create3f',views.createe3f,name='create3f'),
     path('create4a',views.createe4a,name='create4a'),
     path('create4b',views.createe4b,name='create4b'),
     path('create4d',views.createe4d,name='create4d'),
     path('create4f',views.createe4d,name='create4f'),
     path('create5a',views.createe5a,name='create5a'),
     path('create5b',views.createe5b,name='create5b'),
     path('create5d',views.createe5d,name='create5d'),
     path('create5f',views.createe5f,name='create5f'),
     path('create6a',views.createe6a,name='create6a'),
     path('create6b',views.createe6b,name='create6b'),
     path('create6d',views.createe6d,name='create6d'),
     path('create6f',views.createe6f,name='create6f'),
     path('create7a',views.createe7a,name='create7a'),
     path('create7b',views.createe7b,name='create7b'),
     path('create7d',views.createe7d,name='create7d'),
     path('create7f',views.createe7f,name='create7f'),
     path('create8a',views.createe8a,name='create8a'),
     path('create8b',views.createe8b,name='create8b'),
     path('create8d',views.createe8d,name='create8d'),
     path('create8f',views.createe8d,name='create8f'),
     path('create9a',views.createe9a,name='create9a'),
     path('create9b',views.createe9b,name='create9b'),
     path('create9d',views.createe9d,name='create9d'),
     path('create9f',views.createe9f,name='create9f'),
     path('create10a',views.createe10a,name='create10a'),
     path('create10b',views.createe10b,name='create10b'),
     path('create10d',views.createe10d,name='create10d'),
     path('create11a',views.createe11a,name='create11a'),
     path('create11b',views.createe11b,name='create11b'),
     path('create11d',views.createe11d,name='create11d'),
#delete
    path('delete1a/<str:pk>',views.delete1a,name='delete1a'),
    path('delete1b/<str:pk>',views.delete1b,name='delete1b'),
    path('delete1d/<str:pk>',views.delete1d,name='delete1d'),
    path('delete1f/<str:pk>',views.delete1f,name='delete1f'),
    path('delete2a/<str:pk>',views.delete2a,name='delete2a'),
    path('delete2b/<str:pk>',views.delete2b,name='delete2b'),
    path('delete2d/<str:pk>',views.delete2d,name='delete2d'),
    path('delete2f/<str:pk>',views.delete2f,name='delete2f'),
    path('delete3a/<str:pk>',views.delete3a,name='delete3a'),
    path('delete3b/<str:pk>',views.delete3b,name='delete3b'),
    path('delete3d/<str:pk>',views.delete3d,name='delete3d'),
    path('delete3f/<str:pk>',views.delete3f,name='delete3f'),
    path('delete4a/<str:pk>',views.delete4a,name='delete4a'),
    path('delete4b/<str:pk>',views.delete4b,name='delete4b'),
    path('delete4d/<str:pk>',views.delete4d,name='delete4d'),
    path('delete4f/<str:pk>',views.delete4f,name='delete4f'),
    path('delete5a/<str:pk>',views.delete5a,name='delete5a'),
    path('delete5b/<str:pk>',views.delete5b,name='delete5b'),
    path('delete5d/<str:pk>',views.delete5d,name='delete5d'),
    path('delete5f/<str:pk>',views.delete5f,name='delete5f'),
    path('delete6a/<str:pk>',views.delete6a,name='delete6a'),
    path('delete6b/<str:pk>',views.delete6b,name='delete6b'),
    path('delete6d/<str:pk>',views.delete6d,name='delete6d'),
    path('delete6f/<str:pk>',views.delete6f,name='delete6f'),
    path('delete7a/<str:pk>',views.delet7a,name='delete7a'),
    path('delete7b/<str:pk>',views.delete7b,name='delete7b'),
    path('delete7d/<str:pk>',views.delete7d,name='delete7d'),
    path('delete7f/<str:pk>',views.delete7f,name='delete7f'),
    path('delete8a/<str:pk>',views.delete8a,name='delete8a'),
    path('delete8b/<str:pk>',views.delete8b,name='delete8b'),
    path('delete8d/<str:pk>',views.delete8d,name='delete8d'),
    path('delete8f/<str:pk>',views.delete8f,name='delete8f'),
    path('delete9a/<str:pk>',views.delete9a,name='delete9a'),
    path('delete9b/<str:pk>',views.delete9b,name='delete9b'),
    path('delete9d/<str:pk>',views.delete9d,name='delete9d'),
    path('delete9f/<str:pk>',views.delete9f,name='delete9f'),
    path('delete10a/<str:pk>',views.delet10a,name='delete10a'),
    path('delete10b/<str:pk>',views.delete10b,name='delete10b'),
    path('delete10d/<str:pk>',views.delete10d,name='delete10d'),
    path('delete11a/<str:pk>',views.delete11a,name='delete11a'),
    path('delete11b/<str:pk>',views.delete11b,name='delete11b'),
    path('delete11d/<str:pk>',views.delete11d,name='delete11d'),
#delete
    path('update1a/<str:pk>',views.update1a,name='update1a'),
    path('update1b/<str:pk>',views.update1b,name='update1b'),
    path('update1d/<str:pk>',views.update1d,name='update1d'),
    path('update1f/<str:pk>',views.update1f,name='update1f'),
    path('update2a/<str:pk>',views.update2a,name='update2a'),
    path('update2b/<str:pk>',views.update2b,name='update2b'),
    path('update2d/<str:pk>',views.update2d,name='update2d'),
    path('update2f/<str:pk>',views.update2f,name='update2f'),
    path('update3a/<str:pk>',views.update3a,name='update3a'),
    path('update3b/<str:pk>',views.update3b,name='update3b'),
    path('update3d/<str:pk>',views.update3d,name='update3d'),
    path('update3f/<str:pk>',views.update3f,name='update3f'),
    path('update4a/<str:pk>',views.update4a,name='update4a'),
    path('update4b/<str:pk>',views.update4b,name='update4b'),
    path('update4d/<str:pk>',views.update4d,name='update4d'),
    path('update4f/<str:pk>',views.update4f,name='update4f'),
    path('update5a/<str:pk>',views.update5a,name='update5a'),
    path('update5b/<str:pk>',views.update5b,name='update5b'),
    path('update5d/<str:pk>',views.update5d,name='update5d'),
    path('update5f/<str:pk>',views.update5f,name='update5f'),
    path('update6a/<str:pk>',views.update6a,name='update6a'),
    path('update6b/<str:pk>',views.update6b,name='update6b'),
    path('update6d/<str:pk>',views.update6d,name='update6d'),
    path('update6f/<str:pk>',views.update6f,name='update6f'),
    path('update7a/<str:pk>',views.update7a,name='update7a'),
    path('update7b/<str:pk>',views.update7b,name='update7b'),
    path('update7d/<str:pk>',views.update7d,name='update7d'),
    path('update3f/<str:pk>',views.update7f,name='update7f'),
    path('update8a/<str:pk>',views.update8a,name='update8a'),
    path('update8b/<str:pk>',views.update8b,name='update8b'),
    path('update8d/<str:pk>',views.update8d,name='update8d'),
    path('update8f/<str:pk>',views.update8f,name='update8f'),
    path('update9a/<str:pk>',views.update9a,name='update9a'),
    path('update9b/<str:pk>',views.update9b,name='update9b'),
    path('update9d/<str:pk>',views.update9d,name='update9d'),
    path('update9f/<str:pk>',views.update9f,name='update9f'),
    path('update10a/<str:pk>',views.update10a,name='update10a'),
    path('update10b/<str:pk>',views.update10b,name='update10b'),
    path('update10d/<str:pk>',views.update10d,name='update10d'),


     
     path('admin_table/',views.admin_table,name='admin-t'),
     
]
