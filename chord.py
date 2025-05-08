from music21 import key, chord, stream, note, roman
import random



def get_chord_progression_c_minor(note):
    k = key.Key(note, 'minor')
    progression = [
        roman.RomanNumeral('i', k),   # C minor
        roman.RomanNumeral('iv', k),  # F minor
        roman.RomanNumeral('v', k),   # G minor (ou V pour G majeur)
        roman.RomanNumeral('i', k),   # C minor
    ]
    return progression

progression = get_chord_progression_c_minor("D")

for i, ch in enumerate(progression, 1):
    print(f"Accord {i}: {ch.commonName} -> {ch.pitchNames}")
