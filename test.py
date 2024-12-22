import chords_manager


def test_remove_chords_parts():
    print(chords_manager.remove_chord_parts("asdf amaj qwer C#dim fsda"))


def test_only_chords():
    print(chords_manager.is_not_a_chord("A B C D E F G A# C# D# F# G# Ab Bb Db Eb Gb A/A B/B C/C D/D E/E F/F G/G A#/A# C#/C# D#/D# F#/F# G#/G# Ab/Ab Bb/Bb Db/Db Eb/Eb Gb/Gb"))
    print(chords_manager.is_not_a_chord("A- A#+ Abm B4 Bb-11 C7+ C#5m Dm7M D#/A# Db4/7/G#"))
    print(chords_manager.is_not_a_chord("E/G# F#m7        Bm7     E      A"))


if __name__ == "__main__":
    test_remove_chords_parts()
    test_only_chords()
