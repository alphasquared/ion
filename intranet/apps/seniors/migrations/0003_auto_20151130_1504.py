# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('seniors', '0002_auto_20151130_1459')]

    operations = [
        migrations.AlterField(
            model_name='senior',
            name='major',
            field=models.CharField(max_length=100, choices=[
                ('Computer Science', 'Computer Science'), ('Engineering', 'Engineering'), ('Education', 'Education'), (
                    'Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), (
                        'Geology', 'Geology'), ('History', 'History'), ('Literature', 'Literature'), ('English', 'English'), ('Other', 'Other'), (
                            'Language', 'Language'), ('Drama/Theater', 'Drama/Theater'), ('Undecided', 'Undecided'), ('Music', 'Music'), (
                                'Political Science', 'Political Science'), ('Neuroscience', 'Neuroscience'), ('Business', 'Business'), (
                                    'Economics', 'Economics'), ('Communications', 'Communications'), ('World Studies', 'World Studies'),
                ('Art/Art History', 'Art/Art History'), ('Biochemistry', 'Biochemistry'), ('Computer Engineering', 'Computer Engineering'), (
                    'Anthropology', 'Anthropology'), ('Film', 'Film'), ('Atmospheric Science', 'Atmospheric Science'), ('Astronomy', 'Astronomy'), (
                        'Psychology', 'Psychology'), ('Genetics', 'Genetics'), ('Social Work', 'Social Work'), ('Architecture', 'Architecture'), (
                            'Public Policy', 'Public Policy'), ('Classics', 'Classics'), ('Marine Biology', 'Marine Biology'), ('Dance', 'Dance'), (
                                'Philosophy', 'Philosophy'), ('Emergency Health Services', 'Emergency Health Services'),
                ('Animal Science', 'Animal Science'), ('Computer and Video Imaging', 'Computer and Video Imaging'), ('Geography', 'Geography'), (
                    'International Relations', 'International Relations'), ('Foreign Service', 'Foreign Service'), (
                        'Broadcast Journalism', 'Broadcast Journalism'), ('Semitic Studies', 'Semitic Studies'), ('Microbiology', 'Microbiology'), (
                            'Finance', 'Finance'), ('Journalism', 'Journalism'), ('Aeronautics/Astronautics', 'Aeronautics/Astronautics'), (
                                'Pre-med', 'Pre-med'), ('Pre-law', 'Pre-law'), ('Automotive Technician', 'Automotive Technician'), (
                                    'Computer Game Design', 'Computer Game Design'), ('Petroleum Engineering', 'Petroleum Engineering'),
                ('American Studies', 'American Studies'), ('African-American Studies', 'African-American Studies'), ('Linguistics', 'Linguistics'), (
                    'Sociology', 'Sociology'), ('International Finance', 'International Finance'), (
                        'Public Policy in Science and Technology', 'Public Policy in Science and Technology'), (
                            'Information Technology', 'Information Technology'), ('Network Engineering', 'Network Engineering'), (
                                'Environmental Science', 'Environmental Science'), ('Evolutionary Biology', 'Evolutionary Biology'),
                ('Advertising', 'Advertising'), ('Apparel Design', 'Apparel Design'), ('East Asian Studies', 'East Asian Studies'), (
                    'Biomedical Engineering', 'Biomedical Engineering'), ('Policy Analysis and Management', 'Policy Analysis and Management'), (
                        'Videogame Design and Development', 'Videogame Design and Development'), ('Electrical Engineering', 'Electrical Engineering'),
                ('Information Systems', 'Information Systems'), ('Theatre', 'Theatre'), ('Theatre/Directing', 'Theatre/Directing'), (
                    'Leadership', 'Leadership'), ('Design', 'Design'), ('Environmental Thought and Practice', 'Environmental Thought and Practice'), (
                        'Athletic Training', 'Athletic Training'), ('Physical Therapy', 'Physical Therapy'),
                ('Chemical Engineering', 'Chemical Engineering'), ('Athletic Training & Physical Therapy', 'Athletic Training & Physical Therapy'), (
                    'Civil Engineering', 'Civil Engineering'), ('Industrial and Labor Relations', 'Industrial and Labor Relations'), (
                        'Bowling Management', 'Bowling Management'), ('Pre-Dental', 'Pre-Dental'), ('Aerospace Engineering', 'Aerospace Engineering'),
                ('French', 'French'), ('German', 'German'), ('Spanish', 'Spanish'), ('Italian', 'Italian'), ('Chinese', 'Chinese'), (
                    'Operations Research', 'Operations Research'), ('Game Design and Development', 'Game Design and Development'), (
                        'Software Engineering', 'Software Engineering'), ('International Development', 'International Development'), (
                            'Mechanical Engineering', 'Mechanical Engineering'), ('Mathematics & Computer Science', 'Mathematics & Computer Science')
            ]),),
        migrations.DeleteModel(name='Major',),
    ]
