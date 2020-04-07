
cd utils && \
python helper.py && \
python log_agg.py && \
git add . && \
git commit -m "something" && \
git push origin master
cd ..