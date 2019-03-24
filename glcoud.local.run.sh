gcloud ml-engine local train \
--module-name trainer.small-deadspeare \
--package-path ./trainer \
-- \
--train-file deadpoolLines.txt \
--job-dir ./tmp/deadSpeare
