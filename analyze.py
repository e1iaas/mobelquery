import pandas as pd
from collections import Counter

def analyze_text_words(df, text_column='combined_text', top_overall=30, save_reports=True):
    """
    Analyze text in df[text_column] and save word frequency and category files.

    Returns:
        dict: {'all_words': Counter, 'words_by_pos': dict of Counters}
    """
    import spacy
    print("\n🧠 Analyzing text with spaCy...")
    nlp = spacy.load('en_core_web_sm')
    nlp.max_length = 2000000

    all_words = Counter()
    words_by_pos = {}

    pos_names = {
        'NOUN': 'Nouns',
        'VERB': 'Verbs',
        'ADJ': 'Adjectives',
        'ADV': 'Adverbs',
        'PROPN': 'Proper Nouns'
    }

    for idx, text in enumerate(df[text_column].astype(str), 1):
        if idx % 100 == 0:
            print(f" processed {idx}/{len(df)} products...")
        doc = nlp(text)
        for token in doc:
            if not token.is_alpha or token.is_stop:
                continue
            word = token.lemma_.lower()
            pos = token.pos_
            all_words[word] += 1
            if pos not in words_by_pos:
                words_by_pos[pos] = Counter()
            words_by_pos[pos][word] += 1

    print(f"✓ Processed all {len(df)} items")

    # --- Display Top Words ---
    print("\n" + "="*60)
    print(f"🔤 TOP {top_overall} WORDS OVERALL")
    print("="*60)
    for word, count in all_words.most_common(top_overall):
        print(f"  {word:25} {count:6,} times")

    if save_reports:
        # Overall word frequency CSV
        word_df = pd.DataFrame([{'word': w, 'count': c, 'category': 'all'}
                                for w, c in all_words.most_common()])
        word_df.to_csv('word_frequency.csv', index=False)
        print("Saved: word_frequency.csv")

        # Words by POS
        category_data = []
        for pos, counter in words_by_pos.items():
            for word, count in counter.items():
                category_data.append({'word': word, 'count': count, 'category': pos_names.get(pos, pos)})
        category_df = pd.DataFrame(category_data).sort_values('count', ascending=False)
        category_df.to_csv('words_by_category.csv', index=False)
        print("Saved: words_by_category.csv")

        # Text report
        with open("word_analysis_report.txt", 'w', encoding='utf-8') as f:
            f.write("WORD ANALYSIS REPORT\n")
            f.write("="*60 + "\n\n")
            f.write("TOP 100 WORDS OVERALL\n" + "-"*60 + "\n")
            for word, count in all_words.most_common(100):
                f.write(f"{word:30} {count:8,}\n")
            f.write("\n\n")
            for pos, name in pos_names.items():
                if pos in words_by_pos:
                    f.write(f"\n{name.upper()}\n" + "-"*60 + "\n")
                    for word, count in words_by_pos[pos].most_common(50):
                        f.write(f"{word:30} {count:8,}\n")
        print("Saved: word_analysis_report.txt")

    return {
        'all_words': all_words,
        'words_by_pos': words_by_pos
    }
