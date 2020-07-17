from dataclasses import field, dataclass

from traktor_nml_utils.xmldataclass import XMLdataclass

XML = """
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<NML VERSION="19">
  <HEAD COMPANY="www.native-instruments.com" PROGRAM="Traktor"/>
  <MUSICFOLDERS/>
  <COLLECTION ENTRIES="1">
    <ENTRY MODIFIED_DATE="2019/10/19" MODIFIED_TIME="13047" LOCK="1" LOCK_MODIFICATION_TIME="2019-08-23T21:27:21" AUDIO_ID="AMARERERERERERERERERERERERA92ktc3N20taZ9y0ta3NzEtpcsz97e3e3Vvtqt393d/v3Wnsmd////////////////////////zarYzdzarYp6uqnYqN3arayL3vzp/qzPv7/5zf393qlsVYu1NWZUI2RWZUI1lYh3KGmrm82Sr/////////////////3+///73/////////r////////+/v7+///v/4f//f/5b//////Xx7qbj////////////////////////////+zf////u////////////qiHxoWqiXxoWIyJiJm6eXyKd6VypnNaVyp3QREREREREREREA==" TITLE="Dubstep 1" ARTIST="Loopmasters">
      <LOCATION DIR="/:Library/:Application Support/:Native Instruments/:Traktor 2/:Factory Sounds/:" FILE="Loopmasters_Dubstep1.mp3" VOLUME="osx" VOLUMEID="osx"/>
      <MODIFICATION_INFO AUTHOR_TYPE="user"/>
      <INFO BITRATE="189720" GENRE="Dubstep" COMMENT="Tracks by www.loopmasters.com" COVERARTID="113/R1PI3ZDLWQMLAAASJ4B2AQZXI1ZD" KEY="10m" PLAYTIME="193" PLAYTIME_FLOAT="192.078369" IMPORT_DATE="2010/8/16" RELEASE_DATE="2010/1/1" FLAGS="28" FILESIZE="5040"/>
      <TEMPO BPM="139.999924" BPM_QUALITY="100.000000"/>
      <LOUDNESS PEAK_DB="-2.782080" PERCEIVED_DB="0.000000" ANALYZED_DB="-2.000000"/>
      <MUSICAL_KEY VALUE="12"/>
      <CUE_V2 NAME="AutoGrid" DISPL_ORDER="0" TYPE="4" START="52.315876" LEN="0.000000" REPEATS="-1" HOTCUE="0"/>
      <CUE_V2 NAME="n.n." DISPL_ORDER="0" TYPE="0" START="52.315876" LEN="0.000000" REPEATS="-1" HOTCUE="7"/>
      <CUE_V2 NAME="n.n." DISPL_ORDER="0" TYPE="0" START="52.315876" LEN="0.000000" REPEATS="-1" HOTCUE="6"/>
    </ENTRY>
  </COLLECTION>
</NML>
"""


# def test_xml_dataclass_without_xml():
#     @dataclass
#     class NoXMLDataclass(XMLdataclass):
#         x: int = field()
#
#     my_xml_data = NoXMLDataclass(x=1)
#     assert my_xml_data.x == 1


def test_xml_dataclass_withxml():
    @dataclass
    class PlaylistEntry(XMLdataclass):
        filename: str = field(metadata={'xpath': 'PRIMARYKEY/@KEY'})

    dc = PlaylistEntry(filename="asdf")
    assert dc.filename == "asdf"