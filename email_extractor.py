# coding: utf-8
import re
import csv

line = '''
Andre FigueiredoPeter, I rally liked your CV. Could you send me the template?
andre@figueiredo.eng.br
Delete or report this comment1hElias PatelI think this guy Jake Shaw created it back in 2013 https://www.linkedin.com/in/jakebshaw
LikeLike Elias Patel’s commentReplyReply to Elias Patel’s comment
Søren Petersen
Delete or report this comment1hSøren PetersenPlease send a copy thanks. spetersen2@msn.com
LikeLike Søren Petersen’s commentReplyReply to Søren Petersen’s comment
Sonia CHARNI
Delete or report this comment1hSonia CHARNIcrystal clear, I really like it ! I might change mine in the same way ....
LikeLike Sonia CHARNI’S commentReplyReply to Sonia CHARNI’S comment
Maria del Carmen Williams
Delete or report this comment1hMaria del Carmen Williamsmay I have it? Carmen-Williams@hotmail.com
LikeLike Maria del Carmen Williams’ commentReplyReply to Maria del Carmen Williams’ comment
Maria del Carmen Williams
Delete or report this comment1hMaria del Carmen Williamsimpressive...16 thousand likes.
LikeLike Maria del Carmen Williams’ commentReplyReply to Maria del Carmen Williams’ comment
Sunil Karnawat
Delete or report this comment1hSunil KarnawatGreat idea and easy to read; thanks for sharing: sunil.karnawat@gmail.com
LikeLike Sunil Karnawat’s commentReplyReply to Sunil Karnawat’s comment
Sarfaraz Khan

Delete or report this comment1hSarfaraz KhanKindly do send me as well skhan479@live.com
LikeLike Sarfaraz Khan’s commentReplyReply to Sarfaraz Khan’s comment
Cihan AKI
Delete or report this comment1hCihan AKII would love to have your template could you send it to me to cihanaki@gmail.com please
LikeLike Cihan AKI’S commentReplyReply to Cihan AKI’S comment
William McGillivray
Delete or report this comment1hWilliam McGillivraylike the simplicity..wouldn't mind a copy webmannie@gmail.com
LikeLike William McGillivray’s commentReplyReply to William McGillivray’s comment
Laura Scaglia
Delete or report this comment1hLaura ScagliaI did smth similar a few years ago, would love to have a look at yours, thanks for sharing at laura.scaglia@hotmail.com, cheers
LikeLike Laura Scaglia’s commentReplyReply to Laura Scaglia’s comment
Casimiro da Silva Santos, MBA
Delete or report this comment1hCasimiro da Silva Santos, MBAHi Peter can you send the template to me casimiro.dasilva@icloud.com
LikeLike Casimiro da Silva Santos, MBA’S commentReplyReply to Casimiro da Silva Santos, MBA’S comment
Shannon O'Brien
Delete or report this comment1hShannon O'Brien Thanks Peter, I'd love to see the slide as well: Shannouk23@yahoo.com
LikeLike Shannon O&#39;Brien’s commentReplyReply to Shannon ;Brien’s comment
Sal Napolitano
Delete or report this comment1hSal Napolitanohi Peter, perfect and well done. Direct, easier and creative.
LikeLike Sal Napolitano’s commentReplyReply to Sal Napolitano’s comment
Michael Stanleigh, CMC, CSP, CSM
Delete or report this comment1hMichael Stanleigh, CMC, CSP, CSMPeter - this is awesome. Would love to see the template. Happy holidays mstanleigh@bia.ca
LikeLike Michael Stanleigh, CMC, CSP, CSM’S commentReplyReply to Michael Stanleigh, CMC, CSP, CSM’S comment
Sachin Patil
Delete or report this comment1hSachin PatilPeter - your template stands out from the rest in both creativity and visual appeal. If you dan share a copy please send to sachin.pat@gmail.com
LikeLike Sachin Patil’s commentReplyReply to Sachin Patil’s comment
Shahid Aziz
Delete or report this comment1hShahid Azizthats very nice. pls send me a copy
LikeLike Shahid Aziz’s commentReplyReply to Shahid Aziz’s comment
Ilaria Di Tommaso
Delete or report this comment1hIlaria Di TommasoThat's brilliant!!! 👍
LikeLike Ilaria Di Tommaso’s commentReplyReply to Ilaria Di Tommaso’s comment
Bret Hehl, PMP

Delete or report this comment1hBret Hehl, PMPGreat stuff, may I have a soft copy, Bret.Hehl@gmail.com, thank you!
LikeLike Bret Hehl, PMP’S commentReplyReply to Bret Hehl, PMP’S comment
sumit gupta
Delete or report this comment1hsumit guptarequest a copy er_sumitgupta@yahoo.com
LikeLike sumit gupta’s commentReplyReply to sumit gupta’s comment
Hari Giri
Delete or report this comment1hHari GiriThis seems to be very interesting so let me have ,plz in my id harig379@gmail.com
LikeLike Hari Giri’s commentReplyReply to Hari Giri’s comment
Shahid Aziz
Delete or report this comment1hShahid Azizmy email address is <aziz.shahid1@gmail.com>
LikeLike Shahid Aziz’s commentReplyReply to Shahid Aziz’s comment
Olaoluwa Ayilegbe
Delete or report this comment1hOlaoluwa AyilegbeI love this concept
LikeLike Olaoluwa Ayilegbe’s commentReplyReply to Olaoluwa Ayilegbe’s comment
Mostafa Helmy
Delete or report this comment1hMostafa HelmyWell done , Please send a copy
LikeLike Mostafa Helmy’s commentReplyReply to Mostafa Helmy’s comment
Yahya Zakaria
Delete or report this comment1hYahya ZakariaGreat concept! Pls share the template on yahya.zakaria@hotmail.com.
LikeLike Yahya Zakaria’s commentReplyReply to Yahya Zakaria’s comment
Nicholas M. Kiulia
Delete or report this comment1hNicholas M. KiuliaThis is a great tool. Kindly share with me the template My email: nicholas.kiulia@yahoo.com
LikeLike Nicholas M. Kiulia’s commentReplyReply to Nicholas M. Kiulia’s comment
Satish Bandapati
Delete or report this comment1hSatish BandapatiNice summary....would appreciate if you can share it at bandapati@gmail.com
LikeLike Satish Bandapati’s commentReplyReply to Satish Bandapati’s comment
Ebers Quinones
Delete or report this comment1hEbers QuinonesVery nice CV slide Peter, good idea, congratulations with the new position and Mary Christmas.
LikeLike Ebers Quinones’ commentReplyReply to Ebers Quinones’ comment
Sigurd Pettersen
Delete or report this comment1hSigurd PettersenHi Peter. This looks like an interesting idea. My email is: sigurd.pettersen@grong-sparebank.no. Wish you a merry christmas and a happy new year.
LikeLike Sigurd Pettersen’s commentReplyReply to Sigurd Pettersen’s comment
Simon Cuthbert
Delete or report this comment1hSimon CuthbertI would appreciate a copy Peter, thank you in advance. sscuthbert@hotmail.com
LikeLike Simon Cuthbert’s commentReplyReply to Simon Cuthbert’s comment
Radhika Saswade
Delete or report this comment1hRadhika SaswadeInteresting. Could you please share a copy with saswade.radhika@gmail.com
LikeLike Radhika Saswade’s commentReplyReply to Radhika Saswade’s comment
John Heijmann
Delete or report this comment1hJohn Heijmann(One of) the best CV 's I ever saw; congratulations and thx for viewing it here
LikeLike John Heijmann’s commentReplyReply to John Heijmann’s comment
Marcel Ma
Delete or report this comment1hMarcel Mahi Peter, could you please send me a templete mxsma@nalco.com
LikeLike Marcel Ma’s commentReplyReply to Marcel Ma’s comment
Marcos Paulo Bertoncelo
Delete or report this comment1hMarcos Paulo BertonceloHello Peter!
Interesting concept, with a clear evolving of your reaches and projects...perfect timeline, please share the file, my email is:… show more
LikeLike Marcos Paulo Bertoncelo’s commentReplyReply to Marcos Paulo Bertoncelo’s comment
Ahmed El Debsy
Delete or report this comment1hAhmed El Debsywonderful Peter .. please share the slide
ahmed.m.eldebsy@gmail.com
LikeLike Ahmed El Debsy’s commentReplyReply to Ahmed El Debsy’s comment
Sreedhar Domakonda
Delete or report this comment1hSreedhar DomakondaGreat idea for a one page profile view. I tinkered with my standard CV to add light visuals to depict profile summary and testing in the market.
LikeLike Sreedhar Domakonda’s commentReplyReply to Sreedhar Domakonda’s comment
Nassima Sai
Delete or report this comment1hNassima Saii would be grateful if you send me a copy.many thanks in advance.
LikeLike Nassima Sai’s commentReplyReply to Nassima Sai’s comment
Seronei Chelulei Cheison
Delete or report this comment1hSeronei Chelulei CheisonGreat idea. Please share
LikeLike Seronei Chelulei Cheison’s commentReplyReply to Seronei Chelulei Cheison’s comment
Ihsan Qureshi
Delete or report this comment1hIhsan QureshiHi sir . Can you send me at ihsan.muet2k12@gmail.com . Thanks in advance
LikeLike Ihsan Qureshi’s commentReplyReply to Ihsan Qureshi’s comment
Jai Prakash Singh
Delete or report this comment1hJai Prakash SinghPlease share the file at singhjaihbti@gmai.com
LikeLike Jai Prakash Singh’s commentReplyReply to Jai Prakash Singh’s comment
Bellaaj Wadii
Delete or report this comment1hBellaaj WadiiIt is an excellent result oriented resume. please share it
LikeLike Bellaaj Wadii’s commentReplyReply to Bellaaj Wadii’s comment
Manan Verma
Delete or report this comment1hManan Vermaplease share in manan.verma.2018@nitie.ac.in
LikeLike Manan Verma’s commentReplyReply to Manan Verma’s comment
Ajay Kumar Gupta
Delete or report this comment1hAjay Kumar GuptaGreat format Peter ...please share with me at ajaygupta_21@yahoo.com
LikeLike Ajay Kumar Gupta’s commentReplyReply to Ajay Kumar Gupta’s comment
Shivani Upadhyay
Delete or report this comment1hShivani UpadhyayReally liked the representation . It will be great to get a copy of it.
LikeLike Shivani Upadhyay’s commentReplyReply to Shivani Upadhyay’s comment
🔵 Renato Silvino
Delete or report this comment1h🔵 Renato SilvinoHi Peter,
could you please send to me too?
Renato.silvino10@gmail.com
thanks
LikeLike 🔵 Renato Silvino’s commentReplyReply to 🔵 Renato Silvino’s comment11 person likes 🔵 Renato Silvino’s comment.
Glenn D'Souza
Delete or report this comment1hGlenn D'SouzaExcellent Peter. Please send a copy to glennrd10@gmail.com.
LikeLike Glenn D&#39;Souza’s commentReplyReply to Glenn D&#39;Souza’s comment11 person likes Glenn D&amp;#39;Souza’s comment.
Juan Pablo Aravena
Delete or report this comment1hJuan Pablo AravenaHi Peter!

Could you send me a copy to juan.aravena.g@gmail.com ? I'm really interested !
LikeLike Juan Pablo Aravena’s commentReplyReply to Juan Pablo Aravena’s comment11 person likes Juan Pablo Aravena’s comment.
Ritesh Tiwari
Delete or report this comment1hRitesh Tiwariplease share with me ritesh.mckvie@gmail.com
LikeLike Ritesh Tiwari’s commentReplyReply to Ritesh Tiwari’s comment11 person likes Ritesh Tiwari’s comment.
Patrick Anyanwu-Ebo  MBA,CIA
Delete or report this comment1hPatrick Anyanwu-Ebo MBA,CIANicely done Peter. If you have the time I would like a copy as well it would be greatly appreciated.
Happy Holidays.!
LikeLike Patrick Anyanwu-Ebo MBA,CIA’S commentReplyReply to Patrick Anyanwu-Ebo MBA,CIA’S comment
Amitava Roy
Delete or report this comment1hAmitava RoyHi Peter,
Could you send me please too. I like the concept a lot. roy_amitabh@yahoo.com
Thanks
LikeLike Amitava Roy’s commentReplyReply to Amitava Roy’s comment
Domenico Galimi
Delete or report this comment1hDomenico GalimiDear Peter,

Could you be so kind to send me a copy? d.galimi@hotmail.it
LikeLike Domenico Galimi’s commentReplyReply to Domenico Galimi’s comment
Jayaraman Thatchanamurthy
Delete or report this comment1hJayaraman ThatchanamurthyHi Peter
Can you please send to vinoba32@gmail.com
LikeLike Jayaraman Thatchanamurthy’s commentReplyReply to Jayaraman Thatchanamurthy’s comment
Ron B vTwindude
Delete or report this comment1hRon B vTwindudePeter could you send to me at twindude@gmail.com. Please.

This looks like a very interesting way to do a CV.
LikeLike Ron B vTwindude’s commentReplyReply to Ron B vTwindude’s comment
Nadine Rubin
Delete or report this comment1hNadine RubinI think this is a clever format and I would love a copy
LikeLike Nadine Rubin’s commentReplyReply to Nadine Rubin’s comment
Asim Mohammad
Delete or report this comment1hAsim MohammadWell done - can you please send a copy to amohammad@gmail.com? Thanks!
LikeLike Asim Mohammad’s commentReplyReply to Asim Mohammad’s comment
Rodolphe Dugast Rouillé
Delete or report this comment1hRodolphe Dugast RouilléHi Peter,
If you dont mind sharing a copy of the file at rodolphedr@yahoo.com, I'd be thankful. Great presentation.
Kind regards and thanks
R
LikeLike Rodolphe Dugast Rouillé’s commentReplyReply to Rodolphe Dugast Rouillé’s comment
Patricia Polenz, MAIOP
Delete or report this comment1hPatricia Polenz, MAIOPwould love a copy, ppolenzfpt@gmail.com
LikeLike Patricia Polenz, MAIOP’S commentReplyReply to Patricia Polenz, MAIOP’S comment
Nicholas Trowell
Delete or report this comment57mNicholas TrowellHi Peter. Simple and impactful. I like this is a lot. I would be very grateful if you could share this with me. nicktrowell@yahoo.co.uk

Merry… show more
LikeLike Nicholas Trowell’s commentReplyReply to Nicholas Trowell’s comment
Leena Thawani
Delete or report this comment53mLeena ThawaniGreat job with this timelime based format. Thank you for generously sharing it!!
LikeLike Leena Thawani’s commentReplyReply to Leena Thawani’s comment
Henry Wahyu Tristanto
Delete or report this comment52mHenry Wahyu Tristantothis is awesomeee!
LikeLike Henry Wahyu Tristanto’s commentReplyReply to Henry Wahyu Tristanto’s comment
Steve Shanck
Delete or report this comment52mSteve ShanckGreat approach. A copy please?
LikeLike Steve Shanck’s commentReplyReply to Steve Shanck’s comment
Michael Phelan
Delete or report this comment51mMichael PhelanNice please send Peter, I have something similar on my LinkedIn Profile
LikeLike Michael Phelan’s commentReplyReply to Michael Phelan’s comment
Henson Sy
Delete or report this comment51mHenson SyLooks great Peter. Appreciate if you could share with me at hensonsy@gmail.com
LikeLike Henson Sy’s commentReplyReply to Henson Sy’s comment
Nguyễn Chí Thành Công
Delete or report this comment49mNguyễn Chí Thành CôngJust 1 word "WoW". Please share me a copy to my email nctcong@gmail.com

Super thanks
LikeLike Nguyễn Chí Thành Công’s commentReplyReply to Nguyễn Chí Thành Công’s comment
Tersur Kange
Delete or report this comment48mTersur KangeYour CV format is outstanding. Never seen something like this before. I would be most grateful for a template or copy to customize mine. Thanks… show more
LikeLike Tersur Kange’s commentReplyReply to Tersur Kange’s comment
3ali Bodreis I علي ابوضريس
Delete or report this comment47m3ali Bodreis I علي ابوضريسHello sir
Please share me a copy via aabudrais@gmail.com
LikeLike 3ali Bodreis I علي ابوضريس’s commentReplyReply to 3ali Bodreis I علي ابوضريس’s comment
Ankur Gupta
Delete or report this comment47mAnkur Guptawow! a copy please to my email id : agupta.ankur@gmail.com
LikeLike Ankur Gupta’s commentReplyReply to Ankur Gupta’s comment
Arun Damodaran
Delete or report this comment47mArun Damodaranexcellent... kindly share arundav@gmail.com
LikeLike Arun Damodaran’s commentReplyReply to Arun Damodaran’s comment
Vasant Fulari
Delete or report this comment47mVasant Fularidear sir kindly send me copy on vdfulari@gmail.com
LikeLike Vasant Fulari’s commentReplyReply to Vasant Fulari’s comment
Deepak kaul
Delete or report this comment46mDeepak kaulThis is excellent way of presenting oneself .. if possible share a copy @ dkaul4u@gmail.com
LikeLike Deepak kaul’s commentReplyReply to Deepak kaul’s comment
Marc de Bruijn
Delete or report this comment46mMarc de BruijnInteresting. I would like to have a copy. marcdebruijnmarcdebruijn@outlook.com
LikeLike Marc de Bruijn’s commentReplyReply to Marc de Bruijn’s comment
Anthony Gacanja, CISA, CISM, PMP, PRINCE2
Delete or report this comment42mAnthony Gacanja, CISA, CISM, PMP, PRINCE2Looks great. Please share.
LikeLike Anthony Gacanja, CISA, CISM, PMP, PRINCE2’s commentReplyReply to Anthony Gacanja, CISA, CISM, PMP, PRINCE2’s comment
Nurein Said Mohammed
Delete or report this comment40mNurein Said MohammedWow! Excellent and eye-catching. Can I have a copy on Nurein.said@gmail.com
LikeLike Nurein Said Mohammed’s commentReplyReply to Nurein Said Mohammed’s comment
Rene Blum
Delete or report this comment39mRene BlumReally interesting. Could you please send me this to r.blum.60@bluewin.ch please? And merry xmas by the way!!
LikeLike Rene Blum’s commentReplyReply to Rene Blum’s comment
Sudip Chatterjee
Delete or report this comment37mSudip ChatterjeeI would like a copy !! Sudip.c18@gmail.com
LikeLike Sudip Chatterjee’s commentReplyReply to Sudip Chatterjee’s comment
Christian Kehne
Delete or report this comment36mChristian KehneFanastic Intro one pager! Would really appreciate if if you can share it with me christiankehne@web.de
Thanks a lot!!!
Merry XMAS!
LikeLike Christian Kehne’s commentReplyReply to Christian Kehne’s comment
Vaisakhan Balachandran
Delete or report this comment35mVaisakhan Balachandraninteresting. please share it in vaisakbalachandran3@gmail.com
LikeLike Vaisakhan Balachandran’s commentReplyReply to Vaisakhan Balachandran’s comment
Arun kumar Paramasivam
Delete or report this comment33mArun kumar ParamasivamGreat in one page. Please share with me to parunkumarcareer@gmail.com
LikeLike Arun kumar Paramasivam’s commentReplyReply to Arun kumar Paramasivam’s comment
OLUFEMI ANTHONY OLALEYE
Delete or report this comment32mOLUFEMI ANTHONY OLALEYEVery Interesting and Standing out, pls share with me via olufemiolaleye5@gmail.com. Thank you
LikeLike OLUFEMI ANTHONY OLALEYE’S commentReplyReply to OLUFEMI ANTHONY OLALEYE’S comment
Amit Karulkar
Delete or report this comment31mAmit KarulkarImpressive. Please send me a copy : karulkaramit72@gmail.com
LikeLike Amit Karulkar’s commentReplyReply to Amit Karulkar’s comment
Rahul Gupta
Delete or report this comment30mRahul Guptavery innovative idea... please share a copy @ guptarahul_89@yahoo.com
LikeLike Rahul Gupta’s commentReplyReply to Rahul Gupta’s comment
Manish Keshavan
Delete or report this comment28mManish Keshavancan i please have a copy @ manish.keshavan@gmail.com
LikeLike Manish Keshavan’s commentReplyReply to Manish Keshavan’s comment
Gopi Srinivas Thedlapu
Delete or report this comment28mGopi Srinivas ThedlapuSuperb Peter!! Awesome intro....
LikeLike Gopi Srinivas Thedlapu’s commentReplyReply to Gopi Srinivas Thedlapu’s comment
Roop Tanwar (PMP)
Delete or report this comment26mRoop Tanwar (PMP)Impressive and interesting..

tanwar.roop@gmail.com
LikeLike Roop Tanwar (PMP)’s commentReplyReply to Roop Tanwar (PMP)’s comment
Murli Gupta
Delete or report this comment25mMurli GuptaPlease Share at murligupta_2007@rediffmail.com
LikeLike Murli Gupta’s commentReplyReply to Murli Gupta’s comment
Oluwaseun Solanke
Delete or report this comment23mOluwaseun SolankeLooks good. Do please share. seun.solanke@gmail.com
LikeLike Oluwaseun Solanke’s commentReplyReply to Oluwaseun Solanke’s comment
Tom Thoenes
Delete or report this comment21mTom Thoeneslooks excellent, Would love to receive a copy at Tom.thoenes@gmail.com.
LikeLike Tom Thoenes’ commentReplyReply to Tom Thoenes’ comment
Jo McCroskey
Delete or report this comment21mJo McCroskeyI've seen this before and am always impressed with it as a summary to go with the full CV. Would also appreciate a copy at… show more
LikeLike Jo McCroskey’s commentReplyReply to Jo McCroskey’s comment
Vineet Garg, PMP
Delete or report this comment21mVineet Garg, PMPInnovative. if possible, could you pls share on Vineet_garg@yahoo.com
LikeLike Vineet Garg, PMP’S commentReplyReply to Vineet Garg, PMP’S comment
Daragh Killian
Delete or report this comment20mDaragh KillianGreat structure. Dkillian@glanbia.com Thanks v much in advance. Rgds
Daragh Killian
LikeLike Daragh Killian’s commentReplyReply to Daragh Killian’s comment
John Sullivan
Delete or report this comment18mJohn SullivanGreat idea. Pls share if you could. JJS3RD77@gmail.com
LikeLike John Sullivan’s commentReplyReply to John Sullivan’s comment
Stefano Ragazzini
Delete or report this comment18mStefano RagazziniImpressive. Please send me a copy: stefano.ragazzini63@gmail.com
LikeLike Stefano Ragazzini’s commentReplyReply to Stefano Ragazzini’s comment
Ramzi Roy Labban, PhD
Delete or report this comment18mRamzi Roy Labban, PhDRamzilabban@gmail.com thank you
LikeLike Ramzi Roy Labban, PhD’S commentReplyReply to Ramzi Roy Labban, PhD’S comment
Rajiv Mehta, PMP, CSM, 6σ
Delete or report this comment15mRajiv Mehta, PMP, CSM, 6σImpressive.

mrrajivmehta@hotmail.com Thanks.
LikeLike Rajiv Mehta, PMP, CSM, 6σ’s commentReplyReply to Rajiv Mehta, PMP, CSM, 6σ’s comment
Piotr Tomalski
Delete or report this comment14mPiotr TomalskiGreat
Please forward a copy to ptom5020@gmail.com
Thank you
LikeLike Piotr Tomalski’s commentReplyReply to Piotr Tomalski’s comment
Marjorie Bradbury Laing
Delete or report this comment13mMarjorie Bradbury LaingAmazing, highlights your talents very nicely ! Please send me a copy too!
LikeLike Marjorie Bradbury Laing’s commentReplyReply to Marjorie Bradbury Laing’s comment
Nicole Mckinney
Delete or report this comment13mNicole MckinneyWell done! Please share nicole@bcadgroup.com
LikeLike Nicole Mckinney’s commentReplyReply to Nicole Mckinney’s comment
Lauren DeAlexandris
Delete or report this comment11mLauren DeAlexandrisExcellent and fresh perspective. Please share lvlinfante@alumni.wfu.edu
LikeLike Lauren DeAlexandris’ commentReplyReply to Lauren DeAlexandris’ comment
Brian Friborg
Delete or report this comment10mBrian FriborgGreat. Brianfriborg@hotmail.com
LikeLike Brian Friborg’s commentReplyReply to Brian Friborg’s comment
Karan Rangrej
Delete or report this comment9mKaran Rangrejgreat CV.....plz share resume on karanrangrej14@jbims.edu
LikeLike Karan Rangrej’s commentReplyReply to Karan Rangrej’s comment
Admire Simiti
Delete or report this comment9mAdmire Simitisimitiking@gmail.com please share with me too
LikeLike Admire Simiti’s commentReplyReply to Admire Simiti’s comment
Alexander Dieterich
Delete or report this comment8mAlexander DieterichHello Peter. Could you please share this great gem with me as well? Thank you! alexander_dieterich@cotyinc.com
LikeLike Alexander Dieterich’s commentReplyReply to Alexander Dieterich’s comment
Saradha Pudarjunan
Delete or report this comment6mSaradha Pudarjunanvery nice pls send me copy to saradha_arjun@yahoo.com
LikeLike Saradha Pudarjunan’s commentReplyReply to Saradha Pudarjunan’s comment
Michael Fallon
Delete or report this comment5mMichael FallonReally like this view please send to mfallon726@gmail.com
LikeLike Michael Fallon’s commentReplyReply to Michael Fallon’s comment
Alexandru I. Baltat
Delete or report this comment3mAlexandru I. Baltatlooking great - ab@ofloulabs.com ty
LikeLike Alexandru I. Baltat’s commentReplyReply to Alexandru I. Baltat’s comment
Nishant Mishra
Delete or report this comment53s
'''
line = line.decode('utf-8')
matches = re.findall('[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?', line, re.DOTALL)
print(matches)

for x in matches:
    print x + ','
