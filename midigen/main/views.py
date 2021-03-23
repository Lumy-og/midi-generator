from django.shortcuts import render, redirect
from .forms import Music1
from .models import Midi1
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
import random

# Create your views here.
def index(request):


    if request.method == 'POST':
        form = Music1(request.POST)
        # print(form)
        # message =  request.POST['TaskForm']
        # print(message)

        if form.is_valid():
            form.save()
            return redirect('index')
        # else:
        #     error="Неверная форма"
    else:
        form = Music1()
    context = {
        'form': form
    }
    return render(request, "main/index.html", context)




    # return render(request, "main/index.html")
def jojo(request):
    pool = Midi1.objects.values('tempo').order_by('-id')[0]
    print(type(pool['tempo']))
    print(pool['tempo'])

    pool2 = Midi1.objects.values('instrument').order_by('-id')[0]
    print(pool2)

    pool3 = Midi1.objects.values('repeats').order_by('-id')[0]
    print(pool3)

    pool4 = Midi1.objects.values('track').order_by('-id')[0]
    print(pool4)

    pool5 = Midi1.objects.values('mood').order_by('-id')[0]
    print(pool5)

    pool6 = Midi1.objects.values('melody').order_by('-id')[0]
    print(pool6)




    if pool5['mood']==0:

        list_note = ["G B D", "E", "D", "G", "C", "C E G", "E G B", "D F A",
                    "A C F#", "F A C",
                    "G E C A", "D B G E", "C A F D",
                    "E C A", "D B G", "C A F"
                    ]


        gh = 0
        chord = []
        while gh <=16:

            ggf = random.randint(0,15)

            chord.append(NoteSeq(list_note[ggf]))
            gh=gh+1

        seqlist = []
        h = 0
        while h <= 15:

            h = h + 1

            seqlist.append(chord[h])


        print(seqlist)

        midi3 = Midi(int(pool3['repeats']), tempo=int(pool['tempo']), instrument=int(pool2['instrument']))
        midi3.seq_chords(seqlist, track=0)  # можно добавить time=3 или равное чему ещё угодно
        midi3.write('main/static/sad.mid')

    else:

        print('kek')

        minor = ["A# D F#", "C E A", "G B E", "C F#", "G A# C E", "C F G C", "G A# D F", "C E G D", "C E F# A",
                 "F# B D#"]

        chord2 = []
        gh2 = 0
        seqlist = []
        while gh2 <= 9:
            ggf = random.randint(0, 9)
            chord2.append(NoteSeq(minor[ggf]))
            seqlist.append(chord2[gh2])
            gh2 = gh2 + 1


        print(seqlist)
        midi3 = Midi(int(pool3['repeats']),
                     tempo=int(pool['tempo']),
                     instrument=int(pool2['instrument']))
        midi3.seq_chords(
                            seqlist,
                         track=0
                         )
        midi3.write('main/static/happy.mid')


    return render(request, "main/jojo.html",
                  {'pool': pool})

def formelement(request):
    return render(request, "main/form-element.html")

def appprofile(request):
    return render(request, "main/app-profile.html")