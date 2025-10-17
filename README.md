- faire
````
python3 hey.py
shortcuts sign --mode people-who-know-me --input ./MySC.shortcut --output "MySignedSC.shortcut"
````
# shortcuts-iphone
- ou faire
````
python3 app.py
````
    def _get_icon(self) -> Dict[str, Any]:
        # todo: change me

        if sys.version_info >= (3, 9):
            icon_data = b''
        else:
            icon_data = plistlib.Data(b'')
        return {
            'WFWorkflowIconGlyphNumber': 59511,
            'WFWorkflowIconImageData': icon_data,
            'WFWorkflowIconStartColor': 431817727,
        }


- il faut scaxyz
shortcut-signing-server 
go run . serve localhost:3000
aller à localhost/sign
- il faut go
*sudo apt-get update && sudo apt-get -y install golang-go *
View [docker-osx.md](./docker-osx.md) for an guide how to set up docker with docker-osx to run this program on most non mac machines

- tu dois avoir un burner account icloud pour signer les routines
