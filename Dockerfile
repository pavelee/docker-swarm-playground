FROM docker:dind

COPY --from=library/docker:stable /usr/local/bin/docker /usr/bin/docker

ENTRYPOINT ["dockerd-entrypoint.sh"]