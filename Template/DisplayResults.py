from tkinter import *
from Response import Response
class DisplayResults(Frame):
    # GUI Setup
    def __init__ (self, master):
        # Initialise Questionnaire Class
        Frame.__init__(self, master)
        
        self.pack()
        
        self.retrieveResponse()
    def retrieveResponse(self):
        countAll = 0
        #sumQ1SE = 0.0
        #sumP5Joints = 0

        sumQ1All = 0
        sumQ2All = 0
        sumQ3All = 0
        sumP1All = 0
        sumP2All = 0
        sumP3All = 0
        sumP4All = 0
        sumP5All = 0
        sumP6All = 0

        sumQ1CS = 0
        sumQ2CS = 0
        sumQ3CS = 0
        sumP1CS = 0
        sumP2CS = 0
        sumP3CS = 0
        sumP4CS = 0
        sumP5CS = 0
        sumP6CS = 0

        sumQ1CS_with = 0
        sumQ2CS_with = 0
        sumQ3CS_with = 0
        sumP1CS_with = 0
        sumP2CS_with = 0
        sumP3CS_with = 0
        sumP4CS_with = 0
        sumP5CS_with = 0
        sumP6CS_with = 0

        sumQ1BIS = 0
        sumQ2BIS = 0
        sumQ3BIS = 0
        sumP1BIS = 0
        sumP2BIS = 0
        sumP3BIS = 0
        sumP4BIS = 0
        sumP5BIS = 0
        sumP6BIS = 0

        sumQ1SE = 0
        sumQ2SE = 0
        sumQ3SE = 0
        sumP1SE = 0
        sumP2SE = 0
        sumP3SE = 0
        sumP4SE = 0
        sumP5SE = 0
        sumP6SE = 0

        sumQ1Joints = 0
        sumQ2Joints = 0
        sumQ3Joints = 0
        sumP1Joints = 0
        sumP2Joints = 0
        sumP3Joints = 0
        sumP4Joints = 0
        sumP5Joints = 0
        sumP6Joints = 0

        countCS = 0
        countCS_with = 0
        countBIS = 0
        countSE = 0
        countJoints = 0
        
        import shelve
        db=shelve.open('responsedb')
        respNo = len(db)
        
        for i in range(1,respNo):
            #print(db.get(str(i)))
            Ans = db.get(str(i))
            countAll +=1
            sumQ1All += Ans.q1
            sumQ2All += Ans.q2
            sumQ3All += Ans.q3
            sumP1All += Ans.pr1
            sumP2All += Ans.pr2
            sumP3All += Ans.pr3
            sumP4All += Ans.pr4
            sumP5All += Ans.pr5
            sumP6All += Ans.pr6
            if Ans.prog == "CS":
                countCS +=1
                sumQ1CS += Ans.q1
                sumQ2CS += Ans.q2
                sumQ3CS += Ans.q3
                sumP1CS += Ans.pr1
                sumP2CS += Ans.pr2
                sumP3CS += Ans.pr3
                sumP4CS += Ans.pr4
                sumP5CS += Ans.pr5
                sumP6CS += Ans.pr6
            if Ans.prog == "CS with":
                countCS_with +=1
                sumQ1CS_with += Ans.q1
                sumQ2CS_with += Ans.q2
                sumQ3CS_with += Ans.q3
                sumP1CS_with += Ans.pr1
                sumP2CS_with += Ans.pr2
                sumP3CS_with += Ans.pr3
                sumP4CS_with += Ans.pr4
                sumP5CS_with += Ans.pr5
                sumP6CS_with += Ans.pr6
            if Ans.prog == "BIS":
                countBIS +=1
                sumQ1BIS += Ans.q1
                sumQ2BIS += Ans.q2
                sumQ3BIS += Ans.q3
                sumP1BIS += Ans.pr1
                sumP2BIS += Ans.pr2
                sumP3BIS += Ans.pr3
                sumP4BIS += Ans.pr4
                sumP5BIS += Ans.pr5
                sumP6BIS += Ans.pr6
            if Ans.prog == "SE":
                countSE +=1
                sumQ1SE += Ans.q1
                sumQ2SE += Ans.q2
                sumQ3SE += Ans.q3
                sumP1SE += Ans.pr1
                sumP2SE += Ans.pr2
                sumP3SE += Ans.pr3
                sumP4SE += Ans.pr4
                sumP5SE += Ans.pr5
                sumP6SE += Ans.pr6
            if Ans.prog == "Joints":
                countJoints +=1
                sumQ1Joints += Ans.q1
                sumQ2Joints += Ans.q2
                sumQ3Joints += Ans.q3
                sumP1Joints += Ans.pr1
                sumP2Joints += Ans.pr2
                sumP3Joints += Ans.pr3
                sumP4Joints += Ans.pr4
                sumP5Joints += Ans.pr5
                sumP6Joints += Ans.pr6
        db.close

        if countAll > 0:
            Q1All = sumQ1All/countAll
            Q2All = sumQ2All/countAll
            Q3All = sumQ3All/countAll
        else:
            Q1All = 0
            Q2All = 0
            Q3All = 0
        if countCS > 0:
            CSQ1 = sumQ1CS/countCS
            CSQ2 = sumQ2CS/countCS
            CSQ3 = sumQ3CS/countCS
        else:
            CSQ1 = 0
            CSQ2 = 0
            CSQ3 = 0
        if countCS_with > 0:
            CS_withQ1 = sumQ1CS_with/countCS_with
            CS_withQ2 = sumQ2CS_with/countCS_with
            CS_withQ3 = sumQ3CS_with/countCS_with
        else:
            CS_withQ1 = 0
            CS_withQ2 = 0
            CS_withQ3 = 0
        if countBIS > 0:
            BISQ1 = sumQ1BIS/countBIS
            BISQ2 = sumQ2BIS/countBIS
            BISQ3 = sumQ3BIS/countBIS
        else:
            BISQ1 = 0
            BISQ2 = 0
            BISQ3 = 0
        if countSE > 0:
            SEQ1 = sumQ1SE/countSE
            SEQ2 = sumQ2SE/countSE
            SEQ3 = sumQ3SE/countSE
        else:
            SEQ1 = 0
            SEQ2 = 0
            SEQ3 = 0
        if countJoints > 0:
            JointsQ1 = sumQ1Joints/countJoints
            JointsQ2 = sumQ2Joints/countJoints
            JointsQ3 = sumQ3Joints/countJoints
        else:
            JointsQ1 = 0
            JointsQ2 = 0
            JointsQ3 = 0
        if countAll > 0:
            P1All = sumP1All*100/countAll
            P2All = sumP2All*100/countAll
            P3All = sumP3All*100/countAll
            P4All = sumP4All*100/countAll
            P5All = sumP5All*100/countAll
            P6All = sumP6All*100/countAll
        else:
            P1All = 0;
            P2All = 0;
            P3All = 0;
            P4All = 0;
            P5All = 0;
            P6All = 0;
        if countCS > 0:
            P1CS = sumP1CS*100/countCS
            P2CS = sumP2CS*100/countCS
            P3CS = sumP3CS*100/countCS
            P4CS = sumP4CS*100/countCS
            P5CS = sumP5CS*100/countCS
            P6CS = sumP6CS*100/countCS
        else:
            P1CS = 0;
            P2CS = 0;
            P3CS = 0;
            P4CS = 0;
            P5CS = 0;
            P6CS = 0;
        if countCS_with > 0:
            P1CS_with = sumP1CS_with*100/countCS_with
            P2CS_with = sumP2CS_with*100/countCS_with
            P3CS_with = sumP3CS_with*100/countCS_with
            P4CS_with = sumP4CS_with*100/countCS_with
            P5CS_with = sumP5CS_with*100/countCS_with
            P6CS_with = sumP6CS_with*100/countCS_with
        else:
            P1CS_with = 0;
            P2CS_with = 0;
            P3CS_with = 0;
            P4CS_with = 0;
            P5CS_with = 0;
            P6CS_with = 0;
        if countBIS > 0:
            P1BIS = sumP1BIS*100/countBIS
            P2BIS = sumP2BIS*100/countBIS
            P3BIS = sumP3BIS*100/countBIS
            P4BIS = sumP4BIS*100/countBIS
            P5BIS = sumP5BIS*100/countBIS
            P6BIS = sumP6BIS*100/countBIS
        else:
            P1BIS = 0;
            P2BIS = 0;
            P3BIS = 0;
            P4BIS = 0;
            P5BIS = 0;
            P6BIS = 0;
        if countSE > 0:
            P1SE = sumP1SE*100/countSE
            P2SE = sumP2SE*100/countSE
            P3SE = sumP3SE*100/countSE
            P4SE = sumP4SE*100/countSE
            P5SE = sumP5SE*100/countSE
            P6SE = sumP6SE*100/countSE
        else:
            P1SE = 0;
            P2SE = 0;
            P3SE = 0;
            P4SE = 0;
            P5SE = 0;
            P6SE = 0;
        if countJoints > 0:
            P1Joints = sumP1Joints*100/countJoints
            P2Joints = sumP2Joints*100/countJoints
            P3Joints = sumP3Joints*100/countJoints
            P4Joints = sumP4Joints*100/countJoints
            P5Joints = sumP5Joints*100/countJoints
            P6Joints = sumP6Joints*100/countJoints
        else:
            P1Joints = 0;
            P2Joints = 0;
            P3Joints = 0;
            P4Joints = 0;
            P5Joints = 0;
            P6Joints = 0;
        self.txtDisplay = Text(self, height=14,width=85)
        self.txtDisplay.tag_configure('boldfont', font =('MS', 8, 'bold'))
        self.txtDisplay.tag_configure('normfont', font =('MS', 8))
        
        tabResults = ""
        tabResults += ("\t" + "\t" + "\t" + "\t" + "\t")
        self.txtDisplay.insert(END, "Degree Programme" + tabResults + "ALL" + "\t"
        + "CS" + "\t" + "CS with" + "\t" + "BIS" + "\t"
        + "SE" + "\t" + "Joints" +'\n', 'boldfont')
        self.txtDisplay.insert(END, "Number of Responses:" + tabResults + str(countAll)
        + "\t" + str(countCS) + "\t" + str(countCS_with) + "\t" +
        str(countBIS)+ "\t"+ str(countSE) + "\t"+ str(countJoints)
        +'\n', 'normfont')

        self.txtDisplay.insert(END, "Team experience:"+'\n','boldfont')
        self.txtDisplay.insert(END, "Score (4 - strongly agree, 1 - strongly disagree)"+'\n','normfont')
        self.txtDisplay.insert(END, "1. Our team worked together effectivley" + tabResults + "%.1f" % Q1All
        + "\t" + "%.1f" % CSQ1  + "\t" + "%.1f" % CS_withQ1 + "\t" +
       "%.1f" % BISQ1+ "\t"+ "%.1f" % SEQ1 + "\t"+ "%.1f" % JointsQ1
        +'\n', 'normfont')
        self.txtDisplay.insert(END, "2. Our team produced good quality products?" + tabResults + "%.1f" % Q2All
        + "\t" + "%.1f" % CSQ2  + "\t" + "%.1f" % CS_withQ2 + "\t" +
       "%.1f" % BISQ2+ "\t"+ "%.1f" % SEQ2 + "\t"+ "%.1f" % JointsQ2
        +'\n', 'normfont')
        self.txtDisplay.insert(END, "3. Our team produced good quality products?" + tabResults + "%.1f" % Q3All
        + "\t" + "%.1f" % CSQ3  + "\t" + "%.1f" % CS_withQ3 + "\t" +
       "%.1f" % BISQ3+ "\t"+ "%.1f" % SEQ3 + "\t"+ "%.1f" % JointsQ3
        +'\n'+'\n', 'normfont')
        self.txtDisplay.insert(END, "Problem Experience:"+'\n','boldfont')
        self.txtDisplay.insert(END, "Poor Communication" + tabResults + "%d" % P1All +
        "% \t" + "%d" % P1CS + "% \t" + "%d" % P1CS_with + "% \t"
        + "%d" % P1BIS + "% \t" + "%d" % P1SE + "% \t" + "%d" %
        P1Joints + "% \n", 'normfont')
        
        self.txtDisplay.pack()
# Main
root = Tk()
root.title("Display Results")
app = DisplayResults(root)
root.mainloop()
