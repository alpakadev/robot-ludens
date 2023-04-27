# tic-tac-toe

## Organisation des Projekts

Jedes Team hat erstmal einen eigenen Branch zum sammeln und organisieren von Code. Wenn ein Team mit einem Modul oder Submodul fertig ist bzw. wenn wir uns auf eine Projekt Struktur geeinigt haben können die einzelnen Branches mit dem Main Branch gemerged werden.
Für die Versionierung eurer Branches könnt ihr gerne eigene Tags erstellen (z. B. bewegung-0.1.0 oder strategie-<modulname>), damit kein Durcheinander entsteht und einzelne Branches immer direkt zugeordnet werden können.

Das Projekt ist für alle eingeloggten Nutzer*innen einsehbar, achtet also bitte darauf, nur in die von euch genutzten Branches zu pushen und keine anderen Branches zu beeinflussen.

## gitignore

Es ist nützlich eine .gitignore Datei in eurer lokalen Entwicklungsumgebung einzurichten, um Dateien, die nicht mehr verändert werden (z. B. Schnittstellen oder Klassen, die von anderen Modulen importiert wurden) nicht doppelt hochzuladen oder zu überschreiben.
Auch für das Projekt unwichtige Dateien wie Logs oder externe Python Module sollten von Commits ausgeschlossen werden.
Auf keinen Fall Dateien mit sensiblen Daten (z. B. Passwörter oder Keys) in das Repository hochladen.

## Viel Erfolg!

```
cd existing_repo
git remote add origin https://git.uni-due.de/robot-ludens/tic-tac-toe.git
git branch -M <euer Branch>
```

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

***
