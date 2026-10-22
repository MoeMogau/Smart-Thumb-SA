# SmartThumb SA — AI Recognition Results

Five product images were analysed using Amazon Rekognition `DetectLabels` (`MaxLabels=10`, `MinConfidence=75`). Labels are suggestions, not verified product classifications.

| Image | Key detected labels | Outcome |
|---|---|---|
| `Tabi Ballerinas 6-Gelb.jpg` | Clothing (100%), Footwear (100%), Shoe (100%), High Heel (97.48%) | Labels returned; JSON generated |
| `#donnevieamonpinterest.jpg` | Clothing (100%), Footwear (100%), Shoe (100%), Sneaker (100%) | Labels returned; JSON generated |
| `Sofa chair.jpg` | Couch (100%), Cushion (100%), Furniture (100%), Home Decor (100%) | Labels returned; JSON generated |
| `sweartshirt.jpg` | Clothing (100%), Knitwear (100%), Sweater (100%), Sweatshirt (100%) | Labels returned; JSON generated |
| `Sneakers-puma.jpg` | Clothing (100%), Footwear (100%), Shoe (100%), Sneaker (100%) | Labels returned; JSON generated |

## Findings

- AI labels and metadata were generated for all five tested images (5/5).
- Specific labels may be inaccurate even when confidence is high (e.g., multiple shoe styles for one product).
- The results reflect a small sample; label usefulness has not been independently scored by reviewers.

## Processing Summary

- **Mean file-size reduction:** 72.50% across five images.
- **Images meeting ≥50% reduction target:** 4/5.
- **Thumbnail size:** All five outputs fit within 300 × 300 pixels.
- **Lambda duration:** Only two verified values available (1113.51 ms and 982.24 ms); the remaining durations are blank in the CSV.

## Invalid-file test

Uploading `test1.txt` triggered Lambda. Pillow logged `UnidentifiedImageError`; the invocation failed. Detection is confirmed, but graceful handling is not yet implemented.

## Data files

- `results/processing_metrics.csv`: measured image dimensions, bytes, reductions, and available durations.
- `results/ai_label_results.csv`: one row per detected label and confidence score.
- `results/ai_label_results.json`: per-image structured AI results.
