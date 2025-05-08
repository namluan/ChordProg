from midiutil import MIDIFile


def export_midi(progression, filename="test_prog"):
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTrackName(track, time, "Chord Track")
    midi.addTempo(track, time, 130)
    for chord_obj in progression:
        for pitch in chord_obj.pitches:
            midi.addNote(track, 0, pitch.midi, time, 1, 100)
        time += 1
    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)