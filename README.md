[!["Live" Deployment][github-ci-workflow]](#) [![Uptime Kuma Status][uptime-kuma-status]](#)
 # Personal Discord Bot

Mein eigener persönlicher Discord Bot für Dinge wie z.B.
- Benachrichtigungen, wenn neue YouTube-Videos in eine Playlist hochgeladen werden
- Wenn irgendwo neue, wichtige oder interessante News gepostet werden
- weitere Ideen folgen ...

## TODOs / Simple Roadmap (✔️|❌)

✔️ Youtube API implementieren <br>
✔️ Discord verknüpfen und einen Bot draus machen <br>
✔️ Ermöglichen, dass man weitere Playlisten hinzufügen kann (über custom config-Datei) <br>
✔️ Dockerfile erstellen, damit ein Python Server automatisch erstellt wird <br>
✔️ Mention Rollen (@) hinzufügen, wenn neue YT Videos rauskommen?! <br>
✔️ composer.yaml für Docker erstellen <br>
✔️ Deployment automatisieren mit GitHub Actions <br>
✔️ Notification wenn DC Bot Crasht o.ä. über NTFY, private DC msg oder Uptime Kuma <br>
❌ Unnötige Statistiken erheben wie z.B. wie viele Messages schon erfolgreich mit dem Bot verschickt wurden für den Anfang (embed in README für Live Statistiken möglich??) <br>
❌ Verschiedene Rollen erstellen, für verschiedene Notfication Gründe <br>
❌ Überprüfe Twitch ob es Drops für gewisse (definierbare) Spiele gibt <br>
❌ Suchen nach Youtube Videos die nicht in Playlisten sind, sondern irgendwo auf dem Kanal <br>
❌ Simple Webui um configrationen zu erstellen, ändern, einzusehen (z.B. welche Playlists abgefragt werden sollen) <br>
❌ Livestream "Playlist" auf YouTube scannbar machen wenn möglich <br>

# 
[![built with Codeium][codium-badge]][codium-url]

[github-ci-workflow]: https://github.com/Piket95/personal-discord-bot/actions/workflows/ci.yml/badge.svg
[codium-badge]: https://codeium.com/badges/main
[codium-url]: https://codeium.com
[uptime-kuma-status]: https://kuma.dennisadam.de/api/badge/4/status?upLabel=Running/Online&downLabel=Offline
