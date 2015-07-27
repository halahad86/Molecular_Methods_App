import os
import urllib
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from app.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from app.models import Glossary
from app.models import QQuestion, Answer, MQuestion
import json as simplejson
#Django Q Objects to handle queries
from django.db.models import Q
from search import get_query
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

#  serve pdfs in browser hack
@login_required
def pcr_pdf_view(request):
    with open('static/pdf/PCR.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=PCR.pdf'
        return response
    pdf.closed


@login_required
def lab_manual_pdf_view(request):
    with open('static/pdf/Lab-Manual.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Lab-Manual.pdf'
        return response
    pdf.closed


@login_required
def ligation_pdf_view(request):
    with open('static/pdf/Ligation-and-transformation.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Ligation-and-transformation.pdf'
        return response
    pdf.closed

@login_required
def bws_pdf_view(request):
    with open('static/pdf/Blue-White-Screening.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Blue-White-Screening.pdf'
        return response
    pdf.closed

@login_required
def plasmid_pdf_view(request):
    with open('static/pdf/Plasmid-Miniprep.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Plasmid-Miniprep.pdf'
        return response
    pdf.closed

@login_required
def dna_pdf_view(request):
    with open('static/pdf/DNA-Sequencing.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=static/pdf/DNA-Sequencing.pdf'
        return response
    pdf.closed

@login_required
def qpcr_pdf_view(request):
    with open('static/pdf/Real-time-qPCR.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Real-time-qPCR.pdf'
        return response
    pdf.closed


@login_required
def electro_pdf_view(request):
    with open('static/pdf/Electrophoresis-and-Cleanup.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Electrophoresis-and-Cleanup.pdf'
        return response
    pdf.closed


@login_required
def sa_pdf_view(request):
    with open('static/pdf/Sequence Analysis.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Sequence Analysis.pdf'
        return response
    pdf.closed


@login_required
def lc_pdf_view(request):
    with open('static/pdf/Calculations.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Calculations.pdf'
        return response
    pdf.closed


@login_required
def qpcrexer_pdf_view(request):
    with open('static/pdf/qPCR-Analysis.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=qPCR-Analysis.pdf'
        return response
    pdf.closed


@login_required
def pdexer_pdf_view(request):
    with open('static/pdf/Primer-Design-Exercise.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Primer-Design-Exercise.pdf'
        return response
    pdf.closed


@login_required
def rmexer_pdf_view(request):
    with open('static/pdf/Restriction-Mapping-Exercise.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Restriction-Mapping-Exercise.pdf'
        return response
    pdf.closed

# end of pdfs in browser


@login_required
def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('index.html', context_dict, context)

@login_required
def revision(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('revision.html', context_dict, context)


@login_required
def labs(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('labs.html', context_dict, context)

@login_required
def pcrlab(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('labs/pcrlab.html', context_dict, context)


@login_required
def ligation(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('labs/ligation.html', context_dict, context)


@login_required
def bwscreening(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('labs/bwscreening.html', context_dict, context)


@login_required
def plasmid(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('labs/plasmid.html', context_dict, context)


@login_required
def dna(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('labs/dna.html', context_dict, context)


@login_required
def quantpcr(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('labs/quantpcr.html', context_dict, context)


@login_required
def primersquizzes(request):
    context= RequestContext(request)

    primersquestions=QQuestion.objects.filter(topic=2).order_by('?')[:15]
    primeranswers=Answer.objects.filter(question__topic=2)
    context_dict={}

    context_dict['questions'] = primersquestions
    context_dict['answers'] = primeranswers
    context_dict['title'] ='PCR & Primers'
    return render_to_response('quizzes/quizzes.html',context_dict,context)


@login_required
def checkans(request):

    question_number = request.POST.getlist('ques[]')
    checked_boxesAll=[]

    k=1
    while k<=len(question_number):
        st='ans'+str(k)
        checked_boxes = request.POST.getlist(st)
        if(checked_boxes):
            checked_boxesAll.append(checked_boxes[0])
        k=k+1


    answers = Answer.objects.all()
    questions= []
    corr_ans = []
    user_ans = []

    for q in question_number:
        questionObj=QQuestion.objects.get(number=q)
        questions.append(questionObj)

    score=0
    outof=len(question_number)
    i=0
    j=0
    while i<len(checked_boxesAll):
        try:
            us_ans=Answer.objects.get(question=questions[j], number=checked_boxesAll[i])
            i+=1
            if (us_ans.correct==True):
                score+=1
        except Answer.DoesNotExist:
            us_ans="No Answer Specified"

        user_ans.append(us_ans)
        j+=1

    length = len(checked_boxesAll)
    while length<len(question_number):
        user_ans.append("No Answer Specified")
        length+=1

    for q in questions:
        try:
            cor_ans=Answer.objects.get(question=q, correct=True)
        except Answer.DoesNotExist:
            cor_ans="Correct Answer Not specfied (Error)"

        corr_ans.append(cor_ans)

    data = zip(questions,corr_ans,user_ans)

    if(len(checked_boxesAll)==0):
        data=[]

    context = {'data': data, 'answers' : answers, 'score':score, 'outof':outof}
    return render(request, 'quizzes/checkquizans.html', context)


@login_required
def restrictionquizzes(request):
    context= RequestContext(request)

    restrictionquestions=QQuestion.objects.filter(topic=3).order_by('?')[:15]
    restrictionanswers=Answer.objects.filter(question__topic=3)
    context_dict={}

    context_dict['questions'] = restrictionquestions
    context_dict['answers'] = restrictionanswers
    context_dict['title'] ='Restriction Mapping'
    return render_to_response('quizzes/quizzes.html',context_dict,context)


@login_required
def generalquizzes(request):
    context= RequestContext(request)

    generalquestions=QQuestion.objects.filter(topic=1).order_by('?')[:15]
    generalanswers=Answer.objects.filter(question__topic=1)
    context_dict={}

    context_dict['questions'] = generalquestions
    context_dict['answers'] = generalanswers
    context_dict['title'] ='General Molecular Methods'
    return render_to_response('quizzes/quizzes.html',context_dict,context)


@login_required
def dataquizzes(request):
    context= RequestContext(request)

    generalquestions=QQuestion.objects.filter(topic=4).order_by('?')[:15]
    generalanswers=Answer.objects.filter(question__topic=4)
    context_dict={}

    context_dict['questions'] = generalquestions
    context_dict['answers'] = generalanswers
    context_dict['title'] ='Laboratory Calculations'
    return render_to_response('quizzes/quizzes.html',context_dict,context)


@login_required
def glossary(request):

    context = RequestContext(request)

    context_list = Glossary.objects.order_by('title')
    context_dict={}

    #Created a structure for each letter and then pass it into context_dictionary
    context_dict['terms1'] = context_list.exclude(title__regex=r'^[a-zA-Z]')
    context_dict['termsA'] = context_list.filter(Q(title__istartswith='A'))
    context_dict['termsB'] = context_list.filter(Q(title__istartswith='B'))
    context_dict['termsC'] = context_list.filter(Q(title__istartswith='C'))
    context_dict['termsD'] = context_list.filter(Q(title__istartswith='D'))
    context_dict['termsE'] = context_list.filter(Q(title__istartswith='E'))
    context_dict['termsF'] = context_list.filter(Q(title__istartswith='F'))
    context_dict['termsG'] = context_list.filter(Q(title__istartswith='G'))
    context_dict['termsH'] = context_list.filter(Q(title__istartswith='H'))
    context_dict['termsI'] = context_list.filter(Q(title__istartswith='I'))
    context_dict['termsJ'] = context_list.filter(Q(title__istartswith='J'))
    context_dict['termsK'] = context_list.filter(Q(title__istartswith='K'))
    context_dict['termsL'] = context_list.filter(Q(title__istartswith='L'))
    context_dict['termsM'] = context_list.filter(Q(title__istartswith='M'))
    context_dict['termsN'] = context_list.filter(Q(title__istartswith='N'))
    context_dict['termsO'] = context_list.filter(Q(title__istartswith='O'))
    context_dict['termsP'] = context_list.filter(Q(title__istartswith='P'))
    context_dict['termsQ'] = context_list.filter(Q(title__istartswith='Q'))
    context_dict['termsR'] = context_list.filter(Q(title__istartswith='R'))
    context_dict['termsS'] = context_list.filter(Q(title__istartswith='S'))
    context_dict['termsT'] = context_list.filter(Q(title__istartswith='T'))
    context_dict['termsU'] = context_list.filter(Q(title__istartswith='U'))
    context_dict['termsV'] = context_list.filter(Q(title__istartswith='V'))
    context_dict['termsW'] = context_list.filter(Q(title__istartswith='W'))
    context_dict['termsX'] = context_list.filter(Q(title__istartswith='X'))
    context_dict['termsY'] = context_list.filter(Q(title__istartswith='Y'))
    context_dict['termsZ'] = context_list.filter(Q(title__istartswith='Z'))

    return render_to_response('glossary.html', context_dict, context)

@login_required
def videos(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('videos.html',context_dict,context)

@login_required
def revision(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('revision.html',context_dict,context)

@login_required
def converterconcentration(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('calculations/converterconcentration.html',context_dict,context)

@login_required
def converterdilutions(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('calculations/converterdilutions.html',context_dict,context)

@login_required
def convertermass(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('calculations/convertermass.html',context_dict,context)

@login_required
def convertermolarity(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('calculations/convertermolarity.html',context_dict,context)

@login_required
def convertervolume(request):
    context= RequestContext(request)
    context_dict={}
    return render_to_response('calculations/convertervolume.html',context_dict,context)


def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors,

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
        'login/register.html',
        {'user_form': user_form, 'registered': registered},
        context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    context_dict = {}


    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/app/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            context_dict['bad_details'] = True
            return render_to_response('login/login.html', context_dict, context)


    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login/login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/app/')


@login_required
def mapping(request, question_num):
    context = RequestContext(request)
    questionList = MQuestion.objects.order_by('number')[:]
    currQues = MQuestion.objects.get(number = question_num)

    e1 = currQues.enzyme1.split(":")
    e2 = currQues.enzyme2.split(":")
    e3 = currQues.enzyme3.split(":")

    ques = "Uncut plasmid (circular) " + str(float(currQues.size) / 10) + "kb \n"

    ques = ques + e1[0] + "  "
    for i in xrange(1,len(e1)):
        ques = ques + " " + str(float(e1[i]) / 10) + ","
    ques = ques[:-1] + " kb\n"

    ques = ques + e2[0] + "  "
    for i in xrange(1,len(e2)):
        ques = ques + " " + str(float(e2[i]) / 10) + ","
    ques = ques[:-1] + " kb\n"

    ques = ques + e3[0] + "  "
    for i in xrange(1,len(e3)):
        ques = ques + " " + str(float(e3[i]) / 10) + ","
    ques = ques[:-1] + " kb\n"

    ans = currQues.answer
    ans = ans.split(":")
    ans1 = simplejson.dumps(ans[0].split(","))
    ans2 = simplejson.dumps(ans[1].split(","))
    ans3 = simplejson.dumps(ans[2].split(","))
    context_dict = {'size':currQues.size, 'firstMap': ans1, 'secondMap': ans2, 'finalMap': ans3, 'question':ques, 'questions':questionList, 'number':int(question_num)}
    return render_to_response('mapping.html', context_dict, context)


@login_required
def pdf(request, filename):
    fullpath = os.path.join(PDF_PATH, filename)
    response = HttpResponse(file(fullpath).read())
    response['Content-Type'] = 'application/pdf'
    response['Content-disposition'] = 'attachment'
    return response


@login_required
def search(request):
    query_string = ''
    found_entries = None
    if ('term' in request.GET) and request.GET['term'].strip():
        query_string = request.GET['term']

        entry_query = get_query(query_string, ['title'])

        found_entries = Glossary.objects.filter(entry_query).order_by('title')

        return_entries = []

        for entry in found_entries:

            return_entries.append({'label': entry.title, 'value': entry.description})



        return HttpResponse(simplejson.dumps(return_entries), content_type='application/json')

    return HttpResponse(simplejson.dumps([]), content_type='application/json')

def reset_confirm(request, uidb36=None, token=None):
    return password_reset_confirm(request, template_name='resetConfirm.html',
        uidb36=uidb36, token=token, post_reset_redirect=reverse('app:login'))


def reset(request):
    return password_reset(request, template_name='pwdReset.html',
        email_template_name='reset_subject.html',
        subject_template_name='email_title.html',
        post_reset_redirect=reverse('app:login'))

@login_required
def contact(request):
    errors = []
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'molecmeth@gmail.com'),
                ['molecmeth@gmail.com'],
            )
            return render_to_response('thanks.html', context_dict, context)
    return render(request, 'about.html', {'errors': errors})

@login_required
def thanks(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('thanks.html', context_dict, context)