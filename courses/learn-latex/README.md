# LATEX COURSES

## TABLE OF CONTENTS

## GETTING START

Write a report with LaTeX is very usefull. In this short courses, I share you my personnal LaTeX template to write report. But first of all, you need to go on Overleaf website (by clicking on this link <https://fr.overleaf.com>) and create an account (or connect on it). When you do that, go on this link <https://fr.overleaf.com/project> and your normally see all your report, call here "project". You can start a project by clicking on the green button *New project* and select *Empty project*. When you do this, you normaly arrive in a page like this :

![ui](img/ui.PNG)

Here it's the french version, but do not care about it. What is important is the render of this page. You can see lot of things like *Recompile* or *Share*. If you want to allow someone to read or write on your LaTeX document, click on *Share* button and you get a pop up windows like this :

![share_ui](img/share_ui.PNG)

Here you can decide to add by hand people who can read/write on your report by adding their mail (and so by doing this, you send an invitation to the other user who need to accept if he want to read/write). But you can decide to share your report with other people by clicking on *Activate link sharing*. Once you doing this, you can close the pop up windows.

## COVER PAGE

If you don't want a cover page in your report, skip this part. Cover page is important to give a good impression to your reader. Indeed, you need to do a very good cover page with the maximum information you can give. Bellow, I give you an example of a cover page you can do :

![cover_page](img/cover_page.png)

Information you should put here is :
- Object of the paper (LaTex courses report, report of the project of Football Knowledge Graph, ...)
- The name of the project (Football world history project, ...)
- Authors's names
- Student group or working group
- Years when you doing this report
- Logos of the company or school for who your work

To add these informations, follow this code :

```latex
    \begin{titlepage}
		\null	
		\vfill
	
		\centering
		
            %% Title
		
			{\LARGE\scshape LaTeX courses report}

				\vspace{1cm}	
	
			{\Large Football world history courses}

				\vspace{0.75cm}
	
			\textasciitilde
	
				\vspace{0.3cm}

		\begin{center}
		
		    %% Authors
		
		    {\large\scshape Yotlan Le Crom}

				\vspace{0.5cm}
			
			Master ALMA
			
			Years 2021-2022
		\end{center}
		
		\vspace{1cm}
		
		    %% Logo
	
		{\centering
			\includegraphics[scale=0.25]{overleaf_logo.png}
		\par}
	
			\vfill

	\end{titlepage}
```

Notice that it's important to begin and end a LaTeX file with the following commands : `\begin{document}` and `\end{document}`. Moreover, it's important to import lot of package to be able to do lot of things in your report.

## TABLE OF CONTENT

A good report have a table of content to tell to your reader the place of each part with the corresponding page number. Furthermore, it's very easy to create a table of content in LaTeX following this code :

```latex
    %- Sommaire
	\tableofcontents
	\addtocontents{toc}{\protect\thispagestyle{empty}}
	
	\setcounter{page}{1}
	\setlength{\parskip}{1em}

\newpage
```

This code give a table of contents who look like this :

![table_of_contents](img/table_of_contents.png)