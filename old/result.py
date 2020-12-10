"""
Generated with sb3topy
"""
import asyncio
import math            
import random
import time

import engine

class Stage(SpriteBase):
    pass


class skyautoroute(SpriteBase):
    async def onbroadcast_newAutoroute(self, runtime):
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['_routeGrid'].append([10, '"0"'])

        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['_routeBuf'].append([10, '"0"'])




    async def onbroadcast_AutorouteautoRoute(self, runtime):
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['cptScreen'] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]

        self.lists['Params'].append(self.variables['cpt'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactgetMegaSet)
        self.variables['cptWidth'] = self.lists['SkyCompact._RawBuff'][self.variables['Return value'] - 1]

        (e, e)
        (e)
        self.variables['startX'] = self.variables['blkX']
        self.variables['initStaX'] = self.variables['initX']
        (e)
        self.variables['startY'] = self.variables['blkY']
        self.variables['initStaY'] = self.variables['initY']
        (e)
        self.variables['destX'] = self.variables['blkX']
        self.variables['initDestX'] = self.variables['initX']
        (e)
        self.variables['destY'] = self.variables['blkY']
        self.variables['initDestY'] = self.variables['initY']
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
        )
        await util.send_event_awaitable('onbroadcast_' + SkyCompactfetchCpt)
        self.variables['routeDest'] = self.variables['Return value']
        self.variables['i'] = [10, '"0"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['SkyCompact._RawBuff'][(self.variables['routeDest'] + self.variables['i'])
             - 1] = [10, '"0"']
            self.variables['i'] += 4

        self.set_dirty(0)
        if CONDITION:
            self.variables['Return value'] = [10, '"2"']
            return None

        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append(self.variables['cpt'])
            self.lists['Params'].append([10, '"3"'])
            await util.send_event_awaitable('onbroadcast_' + SkyCompactcptIsId)
            self.set_dirty(0)
            if (((self.variables['Return value'] == [10, '"true"'])
             and (self.variables['cptScreen'] == [10, '"12"'])
            )
             and ((self.variables['destX'] == [10, '"2"'])
             and (self.variables['destY'] == [10, '"14"'])
            )
            )
            :
                self.lists['_routeGrid'][(((self.variables['destY'] + 4)
                 * 4)
                 + (self.variables['destX'] + 4)
                )
                 - 1] = [10, '"0"']

            else:
                self.variables['Return value'] = [10, '"1"']
                return None


        (e, e, e, e)
        self.set_dirty(0)
        if CONDITION:
            self.variables['Return value'] = [10, '"1"']
            return None

        (e, e, e, e)
        self.variables['routeData'] = self.variables['Return value']
        (e, e)
        self.variables['routeData'] = self.variables['Return value']
        self.variables['cnt'] = [10, '"0"']
        self.set_dirty(0)
        while True:
            self.lists['SkyCompact._RawBuff'][(self.variables['routeDest'] + self.variables['cnt'])
             - 1] = self.lists['_routeBuf'][(self.variables['routeData'] + self.variables['cnt'])
             - 1]

            self.lists['SkyCompact._RawBuff'][(self.variables['routeDest'] + (self.variables['cnt'] + 4)
            )
             - 1] = self.lists['_routeBuf'][(self.variables['routeData'] + (self.variables['cnt'] + 4)
            )
             - 1]

            self.variables['cnt'] += 4
            self.set_dirty(0)
            if CONDITION:
                self.variables['Return value'] = [10, '"0"']
                return None





    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['_routeGrid'] = []
        self.lists['_routeBuf'] = []
        self.lists['_routeDirections'] = []
        self.lists['_logicCommands'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('_routeGrid')
            # data_showlist('_routeBuf')
            # data_showlist('_routeDirections')
            # data_showlist('_logicCommands')
            await self.sleep(5)

        # data_hidelist('_routeGrid')
        # data_hidelist('_routeBuf')
        # data_hidelist('_routeDirections')
        # data_hidelist('_logicCommands')



    async def onbroadcast_Scratchinitialise(self, runtime):
        self.variables['route_grid_width'] = [10, '"42"']
        self.variables['route_grid_height'] = [10, '"26"']
        self.variables['route_grid_size'] = (self.variables['route_grid_width'] * self.variables['route_grid_height'])

        self.lists['_routeDirections'].append([10, '"-1"'])
        self.lists['_routeDirections'].append([10, '"1"'])
        self.lists['_routeDirections'].append([10, '"-42"'])
        self.lists['_routeDirections'].append([10, '"42"'])
        self.lists['_logicCommands'].append([10, '"3"'])
        self.lists['_logicCommands'].append([10, '"2"'])
        self.lists['_logicCommands'].append([10, '"1"'])
        self.lists['_logicCommands'].append([10, '"0"'])



    async def onbroadcast_deleteAutoroute(self, runtime):
        self.lists['_routeGrid'] = []
        self.lists['_routeBuf'] = []




class skycompact(SpriteBase):
    async def onbroadcast_newSkyCompact(self, runtime):
        # pen_setPenColorToColor([9, '"#949494"'])
        # pen_setPenSizeTo(4)
        # pen_up()
        self.variables['x'] = [10, '"-196"']
        self.xpos = X
        await util.send_event_awaitable('onbroadcast_' + DatagetCompactDataFile)
        self.variables['srcBuf'] = self.variables['Return value']
        self.variables['srcPos'] = [10, '"0"']
        ()
        self.variables['_numDataLists'] = self.variables['Return value']
        self.variables['offset'] = [10, '"1"']
        self.set_dirty(0)
        for _ in range(TIMES):
            ()
            self.lists['_dataListLen'].append(self.variables['Return value'])
            self.lists['SkyCompact._DataOffsets'].append(self.variables['offset'])
            self.variables['offset'] += self.variables['Return value']

        self.variables['xStep'] = (4 / 4)

        ()
        self.variables['rawSize'] = self.variables['Return value']
        self.variables['rawPos'] = [10, '"1"']
        ()
        self.variables['srcSize'] = self.variables['Return value']
        self.variables['diskPos'] = (self.variables['srcPos'] + self.variables['srcSize'])

        ("This is what causes the large pause at the start of a game")
        self.variables['lcnt'] = [10, '"1"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.set_dirty(0)
            for _ in range(TIMES):
                ()
                self.lists['_cptSizes'].append(self.variables['Return value'])
                self.set_dirty(0)
                if not (self.variables['Return value'] == [10, '"0"'])

                :
                    ()
                    self.lists['_cptTypes'].append(self.variables['Return value'])
                    self.lists['SkyCompact._Compacts'].append(self.variables['rawPos'])
                    self.set_dirty(0)
                    for _ in range(TIMES):
                        self.lists['SkyCompact._RawBuff'].append(((((self.lists['Hex'].index(str(self.variables['srcBuf'])[((self.variables['srcPos'] * 4)
                         + 4)
                        ]
                        )
                         - 4)
                         * 4)
                         + (self.lists['Hex'].index(str(self.variables['srcBuf'])[((self.variables['srcPos'] * 4)
                         + 4)
                        ]
                        )
                         - 4)
                        )
                         + ((((self.lists['Hex'].index(str(self.variables['srcBuf'])[((self.variables['srcPos'] * 4)
                         + 4)
                        ]
                        )
                         - 4)
                         * 4)
                         + (self.lists['Hex'].index(str(self.variables['srcBuf'])[((self.variables['srcPos'] * 4)
                         + 4)
                        ]
                        )
                         - 4)
                        )
                         * 4)
                        )
                        )
                        self.variables['srcPos'] += 4
                        self.variables['x'] += self.variables['xStep']
                        self.set_dirty(0)
                        if CONDITION:
                            # pen_up()
                            self.xpos += DX
                            self.ypos = Y
                            # pen_down()
                            self.ypos += DY


                    self.variables['rawPos'] += self.lists['_cptSizes'][len(self.lists['_cptSizes'])
                     - 1]


                else:
                    self.lists['SkyCompact._Compacts'].append([10, '"0"'])


            self.variables['lcnt'] += 4

        self.variables['srcPos'] = self.variables['diskPos']
        ()
        self.variables['numDlincs'] = self.variables['Return value']
        self.set_dirty(0)
        for _ in range(TIMES):
            ()
            self.variables['dlincId'] = self.variables['Return value']
            ()
            self.variables['destId'] = self.variables['Return value']
            (s, s)
            self.variables['temp'] = self.lists['SkyCompact._Compacts'][self.variables['Return value'] - 1]

            (s, s)
            self.lists['SkyCompact._Compacts'][self.variables['Return value'] - 1] = self.variables['temp']

        ()
        self.variables['_numSaveIds'] = self.variables['Return value']
        self.set_dirty(0)
        for _ in range(TIMES):
            ()
            self.lists['SkyCompact._SaveIds'].append(self.variables['Return value'])

        self.variables['_resetDataPos'] = self.variables['srcPos']
        ()



    async def onbroadcast_SkyCompactcptIsId(self, runtime):
        self.variables['id'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].append(self.variables['id'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactfetchCpt)
        self.variables['Return value'] = (self.variables['cpt'] == self.variables['Return value'])




    async def onbroadcast_SkyCompactfetchCpt(self, runtime):
        self.variables['cptId'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.set_dirty(0)
        if CONDITION:
            self.variables['Return value'] = [10, '"0"']
            self.lists['Params'].append([10, '"3"'])
            await util.send_event_awaitable('onbroadcast_' + optimisationstopTimerN)
            self.set_dirty(0)
            if CONDITION:
                answer = input([10, '"Bad fetchCpt result: DEBUG!"'])

            return None

        self.variables['Return value'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['cptId'] / 4)
         + 4)
         - 1]
         + (self.variables['cptId'] % 4)
        )
         - 1]




    async def onbroadcast_SkyCompactfetchCptInfo(self, runtime):
        self.variables['cptId'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['temp'] = (self.lists['SkyCompact._DataOffsets'][((self.variables['cptId'] / 4)
         + 4)
         - 1]
         + (self.variables['cptId'] % 4)
        )

        self.variables['elems'] = self.lists['_cptSizes'][self.variables['temp'] - 1]

        self.variables['Return value'] = self.lists['SkyCompact._Compacts'][self.variables['temp'] - 1]




    async def onbroadcast_SkyCompactnameForType(self, runtime):
        self.lists['Params'].append([10, '"SkyCompact.nameForType"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_SkyCompactgetSub(self, runtime):
        self.variables['mode'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['Return value'] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + (4 + (self.variables['mode'] / 4)
        )
        )
         - 1]

        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append([10, '"SkyCompact.getSub error"'])
                await util.send_event_awaitable('onbroadcast_' + scratchwarning)





    async def onbroadcast_SkyCompactsetSub(self, runtime):
        self.variables['value'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['mode'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + (4 + (self.variables['mode'] / 4)
        )
        )
         - 1] = self.variables['value']
        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append([10, '"SkyCompact.setSub error"'])
                await util.send_event_awaitable('onbroadcast_' + scratchwarning)





    async def onbroadcast_SkyCompactgetGrafixPtr(self, runtime):
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]

        self.variables['gfxBase'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
         + 4)
         - 1]
         + (self.variables['temp'] % 4)
        )
         - 1]

        self.set_dirty(0)
        if (self.variables['gfxBase'] == [10, '"0"'])
        :
            self.variables['Return value'] = [10, '"0"']

        else:
            self.variables['Return value'] = (self.variables['gfxBase'] + self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
             - 1]
            )





    async def onbroadcast_SkyCompactgetMegaSet(self, runtime):
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['Return value'] = (self.variables['cpt'] + (4 + ((self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
         / 4)
         * 4)
        )
        )

        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append([10, '"SkyCompact.getMegaSet error"'])
                await util.send_event_awaitable('onbroadcast_' + scratchwarning)





    async def onbroadcast_SkyCompactgetTurnTable(self, runtime):
        self.variables['dir'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['m'] = (self.variables['cpt'] + (4 + ((self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
         / 4)
         * 4)
        )
        )

        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append([10, '"SkyCompact.getMegaSet error"'])
                await util.send_event_awaitable('onbroadcast_' + scratchwarning)


        self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['m'] + 4)
         - 1]

        self.variables['turnTable'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
         + 4)
         - 1]
         + (self.variables['temp'] % 4)
        )
         - 1]

        self.variables['Return value'] = (self.variables['turnTable'] + (self.variables['dir'] * 4)
        )

        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append([10, '"SkyCompact.getTurnTable: Error"'])
                await util.send_event_awaitable('onbroadcast_' + scratchwarning)





    async def onbroadcast_SkyCompactgetCompactElem(self, runtime):
        self.variables['off'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.set_dirty(0)
        if (self.variables['off'] < [10, '"114"'])
        :
            self.variables['Return value'] = (self.variables['cpt'] + (self.lists['compactOffsets'][(self.variables['off'] + 4)
             - 1]
             / 4)
            )


        else:
            self.variables['off'] += 4
            self.set_dirty(0)
            if (self.variables['off'] < [10, '"44"'])
            :
                self.variables['Return value'] = ((self.variables['cpt'] + 4)
                 + (self.lists['megaSetOffsets'][(self.variables['off'] + 4)
                 - 1]
                 / 4)
                )


            else:
                self.variables['off'] += 4
                self.set_dirty(0)
                if (self.variables['off'] < [10, '"100"'])
                :
                    self.variables['temp'] = self.lists['SkyCompact._RawBuff'][((self.variables['cpt'] + 4)
                     + 4)
                     - 1]

                    self.variables['Return value'] = (self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
                     + 4)
                     - 1]
                     + (self.variables['temp'] % 4)
                    )
                     - 1]
                     + (self.lists['turnTableOffsets'][(self.variables['off'] + 4)
                     - 1]
                     / 4)
                    )


                else:
                    self.variables['off'] += 4
                    self.set_dirty(0)
                    if (self.variables['off'] < [10, '"44"'])
                    :
                        self.variables['Return value'] = ((self.variables['cpt'] + 4)
                         + (self.lists['megaSetOffsets'][(self.variables['off'] + 4)
                         - 1]
                         / 4)
                        )


                    else:
                        self.variables['off'] += 4
                        self.set_dirty(0)
                        if (self.variables['off'] < [10, '"100"'])
                        :
                            self.variables['temp'] = self.lists['SkyCompact._RawBuff'][((self.variables['cpt'] + 4)
                             + 4)
                             - 1]

                            self.variables['Return value'] = (self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
                             + 4)
                             - 1]
                             + (self.variables['temp'] % 4)
                            )
                             - 1]
                             + (self.lists['turnTableOffsets'][(self.variables['off'] + 4)
                             - 1]
                             / 4)
                            )


                        else:
                            self.variables['off'] += 4
                            self.set_dirty(0)
                            if (self.variables['off'] < [10, '"44"'])
                            :
                                self.variables['Return value'] = ((self.variables['cpt'] + 4)
                                 + (self.lists['megaSetOffsets'][(self.variables['off'] + 4)
                                 - 1]
                                 / 4)
                                )


                            else:
                                self.variables['off'] += 4
                                self.set_dirty(0)
                                if (self.variables['off'] < [10, '"100"'])
                                :
                                    self.variables['temp'] = self.lists['SkyCompact._RawBuff'][((self.variables['cpt'] + 4)
                                     + 4)
                                     - 1]

                                    self.variables['Return value'] = (self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
                                     + 4)
                                     - 1]
                                     + (self.variables['temp'] % 4)
                                    )
                                     - 1]
                                     + (self.lists['turnTableOffsets'][(self.variables['off'] + 4)
                                     - 1]
                                     / 4)
                                    )


                                else:
                                    self.variables['off'] += 4
                                    self.set_dirty(0)
                                    if (self.variables['off'] < [10, '"44"'])
                                    :
                                        self.variables['Return value'] = ((self.variables['cpt'] + 4)
                                         + (self.lists['megaSetOffsets'][(self.variables['off'] + 4)
                                         - 1]
                                         / 4)
                                        )


                                    else:
                                        self.variables['off'] += 4
                                        self.set_dirty(0)
                                        if (self.variables['off'] < [10, '"100"'])
                                        :
                                            self.variables['temp'] = self.lists['SkyCompact._RawBuff'][((self.variables['cpt'] + 4)
                                             + 4)
                                             - 1]

                                            self.variables['Return value'] = (self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
                                             + 4)
                                             - 1]
                                             + (self.variables['temp'] % 4)
                                            )
                                             - 1]
                                             + (self.lists['turnTableOffsets'][(self.variables['off'] + 4)
                                             - 1]
                                             / 4)
                                            )


                                        else:
                                            self.variables['off'] += 4












    async def onbroadcast_SkyCompactcreateResetData(self, runtime):
        ("This data is now created as a one-off at intialisation time")



    async def onbroadcast_SkyCompactfindCptId(self, runtime):
        self.lists['Params'].append([10, '"SkyCompact.findCptId"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_SkyCompactgiveNumDataLists(self, runtime):
        self.lists['Params'].append([10, '"SkyCompact.giveNumDataLists"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_SkyCompactgiveDataListLen(self, runtime):
        self.lists['Params'].append([10, '"SkyCompact.giveDataListLen"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_Scratchinitialise(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + DatagetCompactOffsets)
        self.variables['a'] = self.variables['Return value']
        await util.send_event_awaitable('onbroadcast_' + DatagetMegaSetOffsets)
        self.variables['b'] = self.variables['Return value']
        await util.send_event_awaitable('onbroadcast_' + DatagetTurnTableOffsets)
        (e, e, e)



    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['_dataListLen'] = []
        self.lists['_cptTypes'] = []
        self.lists['_cptSizes'] = []
        self.lists['SkyCompact._Compacts'] = []
        self.lists['SkyCompact._RawBuff'] = []
        self.lists['SkyCompact._SaveIds'] = []
        self.lists['compactOffsets'] = []
        self.lists['megaSetOffsets'] = []
        self.lists['turnTableOffsets'] = []
        self.lists['SkyCompact._DataOffsets'] = []
        self.lists['SaveGameData'] = []
        self.variables['srcBuf'] = [10, '""']
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('_dataListLen')
            # data_showlist('_cptTypes')
            # data_showlist('_cptSizes')
            # data_showlist('SkyCompact._Compacts')
            # data_showlist('SkyCompact._RawBuff')
            # data_showlist('SkyCompact._SaveIds')
            # data_showlist('compactOffsets')
            # data_showlist('megaSetOffsets')
            # data_showlist('turnTableOffsets')
            # data_showlist('SkyCompact._DataOffsets')
            # data_showlist('SaveGameData')
            # data_showvariable('srcBuf')
            await self.sleep(5)

        # data_hidelist('_dataListLen')
        # data_hidelist('_cptTypes')
        # data_hidelist('_cptSizes')
        # data_hidelist('SkyCompact._Compacts')
        # data_hidelist('SkyCompact._RawBuff')
        # data_hidelist('SkyCompact._SaveIds')
        # data_hidelist('compactOffsets')
        # data_hidelist('megaSetOffsets')
        # data_hidelist('turnTableOffsets')
        # data_hidelist('SkyCompact._DataOffsets')
        # data_hidelist('SaveGameData')
        # data_hidevariable('srcBuf')




class skycontrol(SpriteBase):
    async def onbroadcast_newControl(self, runtime):
        pass


    async def onbroadcast_newConResource(self, runtime):
        self.lists['Params'].append([10, '"new ConResource"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ConResourceisMouseOver(self, runtime):
        self.lists['Params'].append([10, '"ConResource.isMouseOver"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ConResourcedrawToScreen(self, runtime):
        self.lists['Params'].append([10, '"ConResource.drawToScreen"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_newTextResource(self, runtime):
        self.lists['Params'].append([10, '"new TextResource"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_TextResourceflushForRedraw(self, runtime):
        self.lists['Params'].append([10, '"TextResource.flushForRedraw"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_TextResourcedrawToScreen(self, runtime):
        self.lists['Params'].append([10, '"TextResource.drawToScreen"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_newControlStatus(self, runtime):
        self.lists['Params'].append([10, '"new ControlStatus"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControlStatussetToText(self, runtime):
        self.lists['Params'].append([10, '"ControlStatus.setToText"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControlStatusdrawToScreen(self, runtime):
        self.lists['Params'].append([10, '"ControlStatus.drawToScreen"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControlcreateResource(self, runtime):
        self.lists['Params'].append([10, '"Control.createResource"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControlremovePanel(self, runtime):
        self.lists['Params'].append([10, '"Control.removePanel"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControlinitPanel(self, runtime):
        self.lists['Params'].append([10, '"Control.initPanel"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControldrawMainPanel(self, runtime):
        self.lists['Params'].append([10, '"Control.drawMainPanel"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControldoLoadSavePanel(self, runtime):
        self.lists['Params'].append([10, '"Control.doLoadSavePanel"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControldoControlPanel(self, runtime):
        self.lists['Params'].append([10, '"Control.doControlPanel"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControlloadDescriptions(self, runtime):
        self.lists['Params'].append([10, '"Control.loadDescriptions"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControlloadSaveAllowed(self, runtime):
        self.lists['Params'].append([10, '"Control.loadSaveAllowed"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControlsaveDescriptions(self, runtime):
        self.lists['Params'].append([10, '"Control.saveDescriptions"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControldoAutoSave(self, runtime):
        self.lists['Params'].append([10, '"Control.doAutoSave"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControlsaveGameToFile(self, runtime):
        self.lists['Params'].append([10, '"Control.saveGameToFile"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)
        ()



    async def onbroadcast_ControlquickXRestore(self, runtime):
        self.lists['Params'].append([10, '"Control.quickXRestore"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)
        answer = input([10, '"Enter save game code"'])
        self.xpos = 4
        self.ypos = 4
        self.costume = self.get_costume('loading')
        # looks_gotofrontback()
        self.visible = 1
        self.variables['i'] = util.targets['sky.compact'].variables['saveGameOffset']

        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['SaveGameData'].pop(self.variables['i'] - 1)

        self.variables['j'] = [10, '"0"']
        self.variables['i'] = [10, '"1"']
        self.set_dirty(0)
        while not (self.variables['j'] == (len(answer
        )
         / 4)
        )
        :
            (n, e, "2")
            self.variables['j'] += 4
            self.set_dirty(0)
            for _ in range(TIMES):
                self.lists['SaveGameData'].append(self.lists['SaveGameData'][self.variables['i'] - 1]
                )
                self.variables['i'] += 4

            self.set_dirty(0)
            if CONDITION:
                (n, e, "2")
                self.variables['j'] += 4
                self.variables['diffCtr'] = self.variables['Return value']
                self.set_dirty(0)
                for _ in range(TIMES):
                    (n, e, "2")
                    self.variables['j'] += 4
                    self.lists['SaveGameData'].append(self.variables['Return value'])
                    self.variables['i'] += 4



        (t)
        self.variables['i'] = util.targets['sky.compact'].variables['saveGameOffset']

        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['SaveGameData'].pop(self.variables['i'] - 1)

        self.variables['_SystemVars.pastIntro'] = [10, '"true"']
        self.visible = 0



    async def onbroadcast_ControlrestartGame(self, runtime):
        ("1")
        self.lists['Params'].append(self.variables['_savedMouse'])
        self.lists['Params'].append([10, '"0"'])
        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + MousespriteMouse)
        self.variables['_SystemVars.pastIntro'] = [10, '"true"']



    async def onbroadcast_Controldelay(self, runtime):
        self.lists['Params'].append([10, '"Control.delay"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ControlshowGameQuitMsg(self, runtime):
        self.lists['Params'].append([10, '"Control.showGameQuitMsg"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['reloadList'] = []
        self.lists['SaveCode'] = []
        self.lists['compressed'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('reloadList')
            # data_showlist('SaveCode')
            # data_showlist('compressed')
            await self.sleep(5)

        # data_hidelist('reloadList')
        # data_hidelist('SaveCode')
        # data_hidelist('compressed')
        self.variables['destBuf'] = [10, '""']
        self.visible = 0




class skydisk(SpriteBase):
    async def onbroadcast_newDisk(self, runtime):
        self.lists['_buildList'] = []
        self.lists['SkyCompact._LoadedFilesList'] = []
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['_buildList'].append([10, '"0"'])
            self.lists['SkyCompact._LoadedFilesList'].append([10, '"0"'])

        self.lists['fileNumbers'] = []
        ("Note that dinnerData is just a list of file numbers (names) sorted into order")
        self.variables['_dinnerTableEntries'] = [10, '"1445"']
        self.variables['index'] = [10, '"0"']
        self.set_dirty(0)
        for _ in range(TIMES):
            (e)
            self.lists['fileNumbers'].append(self.variables['Return value'])
            self.variables['index'] += 4




    async def onbroadcast_DiskfileExists(self, runtime):
        self.variables['fileNr'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e)
        self.variables['Return value'] = (self.variables['Return value'] > [10, '"0"'])




    async def onbroadcast_DiskloadFile(self, runtime):
        self.variables['fileNr'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e)
        self.lists['Params'].append(self.variables['Return value'])
        await util.send_event_awaitable('onbroadcast_' + DataloadFile)
        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append((str((str([10, '"File "']) + str(self.variables['fileNr']))
                ) + str([10, '" has no data"']))
                )
                await util.send_event_awaitable('onbroadcast_' + scratcherror)





    async def onbroadcast_DiskloadScriptFile(self, runtime):
        self.variables['fileNr'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].append(self.variables['fileNr'])
        await util.send_event_awaitable('onbroadcast_' + DiskloadFile)



    async def onbroadcast_DiskfnCacheChip(self, runtime):
        self.variables['fList'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['cnt'] = [10, '"0"']
        self.set_dirty(0)
        while not (self.lists['_buildList'][(self.variables['cnt'] + 4)
         - 1]
         == [10, '"0"'])
        :
            self.variables['cnt'] += 4

        self.variables['fCnt'] = [10, '"0"']
        self.set_dirty(0)
        while True:
            self.lists['_buildList'][((self.variables['cnt'] + self.variables['fCnt'])
             + 4)
             - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['fList'] + self.variables['fCnt'])
             - 1]
             % 4)

            self.variables['fCnt'] += 4
            self.set_dirty(0)
            if CONDITION:
                await util.send_event_awaitable('onbroadcast_' + DiskfnCacheFiles)
                return None





    async def onbroadcast_DiskfnCacheFast(self, runtime):
        self.variables['fList'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.set_dirty(0)
        if CONDITION:
            self.variables['cnt'] = [10, '"0"']
            self.set_dirty(0)
            while True:
                self.lists['_buildList'][(self.variables['cnt'] + 4)
                 - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['fList'] + self.variables['cnt'])
                 - 1]
                 % 4)

                self.variables['cnt'] += 4
                self.set_dirty(0)
                if CONDITION:
                    return None






    async def onbroadcast_DiskfnCacheFiles(self, runtime):
        self.variables['targCnt'] = [10, '"0"']
        self.variables['lCnt'] = [10, '"0"']
        self.set_dirty(0)
        while not (self.lists['SkyCompact._LoadedFilesList'][(self.variables['lCnt'] + 4)
         - 1]
         == [10, '"0"'])
        :
            self.variables['bCnt'] = [10, '"0"']
            self.variables['found'] = [10, '"false"']
            self.set_dirty(0)
            while not ((self.lists['_buildList'][(self.variables['bCnt'] + 4)
             - 1]
             == [10, '"0"'])
             or (self.variables['found'] == [10, '"true"'])
            )
            :
                self.set_dirty(0)
                if ((self.lists['_buildList'][(self.variables['bCnt'] + 4)
                 - 1]
                 % 4)
                 == self.lists['SkyCompact._LoadedFilesList'][(self.variables['lCnt'] + 4)
                 - 1]
                )
                :
                    self.variables['found'] = [10, '"true"']

                else:
                    self.variables['bCnt'] += 4


            self.set_dirty(0)
            if (self.variables['found'] == [10, '"true"'])
            :
                self.lists['SkyCompact._LoadedFilesList'][(self.variables['targCnt'] + 4)
                 - 1] = self.lists['SkyCompact._LoadedFilesList'][(self.variables['lCnt'] + 4)
                 - 1]

                self.variables['targCnt'] += 4

            else:
                self.lists['SkyEngine._ItemList'][((self.lists['SkyCompact._LoadedFilesList'][(self.variables['lCnt'] + 4)
                 - 1]
                 % 4)
                 + 4)
                 - 1] = [10, '"0"']

            self.variables['lCnt'] += 4

        self.lists['SkyCompact._LoadedFilesList'][(self.variables['targCnt'] + 4)
         - 1] = [10, '"0"']
        self.variables['bCnt'] = [10, '"0"']
        self.set_dirty(0)
        while not (self.lists['_buildList'][(self.variables['bCnt'] + 4)
         - 1]
         == [10, '"0"'])
        :
            self.set_dirty(0)
            if ((self.lists['_buildList'][(self.variables['bCnt'] + 4)
             - 1]
             % 4)
             == [10, '"2047"'])
            :
                self.variables['bCnt'] += 4

            else:
                self.variables['lCnt'] = [10, '"0"']
                self.variables['found'] = [10, '"false"']
                self.set_dirty(0)
                while not ((self.lists['SkyCompact._LoadedFilesList'][(self.variables['lCnt'] + 4)
                 - 1]
                 == [10, '"0"'])
                 or (self.variables['found'] == [10, '"true"'])
                )
                :
                    self.set_dirty(0)
                    if CONDITION:
                        self.variables['found'] = [10, '"true"']

                    self.variables['lCnt'] += 4

                self.set_dirty(0)
                if (self.variables['found'] == [10, '"true"'])
                :
                    self.variables['bCnt'] += 4

                else:
                    self.lists['SkyCompact._LoadedFilesList'][(self.variables['targCnt'] + 4)
                     - 1] = (self.lists['_buildList'][(self.variables['bCnt'] + 4)
                     - 1]
                     % 4)

                    self.variables['targCnt'] += 4
                    self.lists['SkyCompact._LoadedFilesList'][(self.variables['targCnt'] + 4)
                     - 1] = [10, '"0"']
                    self.lists['Params'].append((self.lists['_buildList'][(self.variables['bCnt'] + 4)
                     - 1]
                     % 4)
                    )
                    await util.send_event_awaitable('onbroadcast_' + diskloadSprite)
                    self.lists['SkyEngine._ItemList'][((self.lists['_buildList'][(self.variables['bCnt'] + 4)
                     - 1]
                     % 4)
                     + 4)
                     - 1] = self.variables['Return value']
                    self.variables['bCnt'] += 4



        self.lists['_buildList'][7 - 1] = [10, '"0"']



    async def onbroadcast_DiskrefreshFilesList(self, runtime):
        self.variables['cnt'] = [10, '"1"']
        self.set_dirty(0)
        while not (self.lists['SkyCompact._LoadedFilesList'][self.variables['cnt'] - 1]
         == [10, '"0"'])
        :
            self.lists['SkyEngine._ItemList'][((self.lists['SkyCompact._LoadedFilesList'][self.variables['cnt'] - 1]
             % 4)
             + 4)
             - 1] = [10, '"0"']
            self.variables['cnt'] += 4

        self.variables['cnt'] = [10, '"1"']
        self.set_dirty(0)
        while not (self.lists['Generic list'][self.variables['cnt'] - 1]
         == [10, '"0"'])
        :
            self.lists['SkyCompact._LoadedFilesList'][self.variables['cnt'] - 1] = self.lists['Generic list'][self.variables['cnt'] - 1]

            self.lists['Params'].append((self.lists['SkyCompact._LoadedFilesList'][self.variables['cnt'] - 1]
             % 4)
            )
            await util.send_event_awaitable('onbroadcast_' + diskloadSprite)
            self.lists['SkyEngine._ItemList'][((self.lists['SkyCompact._LoadedFilesList'][self.variables['cnt'] - 1]
             % 4)
             + 4)
             - 1] = self.variables['Return value']
            self.variables['cnt'] += 4

        self.lists['SkyCompact._LoadedFilesList'][self.variables['cnt'] - 1] = [10, '"0"']



    async def onbroadcast_DiskfnMiniLoad(self, runtime):
        self.variables['fileNum'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['cnt'] = [10, '"1"']
        self.set_dirty(0)
        while not (self.lists['SkyCompact._LoadedFilesList'][self.variables['cnt'] - 1]
         == [10, '"0"'])
        :
            self.set_dirty(0)
            if CONDITION:
                return None

            self.variables['cnt'] += 4

        self.lists['SkyCompact._LoadedFilesList'][self.variables['cnt'] - 1] = (self.variables['fileNum'] % 4)

        self.lists['SkyCompact._LoadedFilesList'][(self.variables['cnt'] + 4)
         - 1] = [10, '"0"']
        self.lists['Params'].append(self.variables['fileNum'])
        await util.send_event_awaitable('onbroadcast_' + DiskloadFile)
        self.lists['SkyEngine._ItemList'][((self.lists['SkyCompact._LoadedFilesList'][self.variables['fileNum'] - 1]
         % 4)
         + 4)
         - 1] = self.variables['Return value']



    async def onbroadcast_DiskdumpFile(self, runtime):
        self.lists['Params'].append([10, '"Disk.dumpFile"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_DiskdetermineGameVersion(self, runtime):
        self.variables['Return value'] = [10, '"348"']



    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['_buildList'] = []
        self.lists['SkyCompact._LoadedFilesList'] = []
        self.lists['fileNumbers'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('_buildList')
            # data_showlist('SkyCompact._LoadedFilesList')
            # data_showlist('fileNumbers')
            await self.sleep(5)

        # data_hidelist('_buildList')
        # data_hidelist('SkyCompact._LoadedFilesList')
        # data_hidelist('fileNumbers')



    async def onbroadcast_deleteDisk(self, runtime):
        ()



    async def onbroadcast_DiskfnFlushBuffers(self, runtime):
        ()



    async def onbroadcast__diskloadSprite(self, runtime):
        self.variables['fileNr'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].append(self.variables['fileNr'])
        await util.send_event_awaitable('onbroadcast_' + DiskloadFile)
        self.set_dirty(0)
        if not (len(self.variables['Return value'])
         == [10, '"44"'])

        :
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append((str((str([10, '"File "']) + str(self.variables['fileNr']))
                ) + str([10, '" is not a sprite"']))
                )
                await util.send_event_awaitable('onbroadcast_' + scratcherror)

            self.variables['Return value'] = [10, '"0"']

        else:
            self.variables['fileNr'] = (self.variables['fileNr'] % 4)

            self.variables['j'] = ((self.variables['fileNr'] * 4)
             + 4)

            self.variables['i'] = [10, '"1"']
            self.set_dirty(0)
            for _ in range(TIMES):
                self.lists['Sprites.data'][self.variables['j'] - 1] = ((((self.lists['Hex'].index(str(self.variables['Return value'])[self.variables['i']]
                )
                 - 4)
                 * 4)
                 + (self.lists['Hex'].index(str(self.variables['Return value'])[(self.variables['i'] + 4)
                ]
                )
                 - 4)
                )
                 + ((((self.lists['Hex'].index(str(self.variables['Return value'])[(self.variables['i'] + 4)
                ]
                )
                 - 4)
                 * 4)
                 + (self.lists['Hex'].index(str(self.variables['Return value'])[(self.variables['i'] + 4)
                ]
                )
                 - 4)
                )
                 * 4)
                )

                self.variables['i'] += 4
                self.variables['j'] += 4

            self.variables['Return value'] = ((self.variables['fileNr'] * 4)
             + 4)

            self.set_dirty(0)
            if CONDITION:
                self.lists['Sprites.data'][(self.variables['Return value'] + 4)
                 - 1] = (self.lists['Sprites.data'][(self.variables['Return value'] + 4)
                 - 1]
                 - 4)


            self.set_dirty(0)
            if CONDITION:
                self.lists['Sprites.data'][(self.variables['Return value'] + 4)
                 - 1] = (self.lists['Sprites.data'][(self.variables['Return value'] + 4)
                 - 1]
                 - 4)







class skygrid(SpriteBase):
    async def onbroadcast_newGrid(self, runtime):
        self.variables['cnt'] = [10, '"1"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['_gameGrids'][self.variables['cnt'] - 1] = [10, '"0"']
            self.variables['cnt'] += 4




    async def onbroadcast_GridloadGrids(self, runtime):
        self.lists['Grid._GameGrids'] = []
        await util.send_event_awaitable('onbroadcast_' + DatagetGameGrids)
        self.variables['hex'] = self.variables['Return value']
        self.variables['i'] = [10, '"1"']
        self.variables['cnt'] = [10, '"1"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['_gameGrids'][self.variables['cnt'] - 1] = self.variables['i']
            self.set_dirty(0)
            for _ in range(TIMES):
                (e, s, "1")
                self.lists['Grid._GameGrids'].append(self.variables['Return value'])
                self.variables['i'] += 4

            self.variables['cnt'] += 4

        self.variables['hex'] = [10, '""']
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"12459"'])
            await util.send_event_awaitable('onbroadcast_' + SkyCompactfetchCpt)
            self.lists['Params'].append([10, '"256"'])
            self.lists['Params'].append([10, '"280"'])
            self.lists['Params'].append([10, '"1"'])
            self.lists['Params'].append(self.variables['Return value'])
            await util.send_event_awaitable('onbroadcast_' + GridremoveGrid)




    async def onbroadcast_GridremoveObjectFromWalk(self, runtime):
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e)
        self.set_dirty(0)
        if CONDITION:
            (e, e, e)




    async def onbroadcast_GridobjectToWalk(self, runtime):
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e)
        self.set_dirty(0)
        if CONDITION:
            (e, e, e)




    async def onbroadcast_GridplotGrid(self, runtime):
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['width'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['y'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['x'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e, e, s, e)
        self.set_dirty(0)
        if CONDITION:
            (e, e, e)




    async def onbroadcast_GridremoveGrid(self, runtime):
        self.variables['cpt'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['width'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['y'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['x'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e, e, e, e)
        self.set_dirty(0)
        if CONDITION:
            (e, e, e)




    async def onbroadcast_GridgiveGrid(self, runtime):
        self.variables['pScreen'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.set_dirty(0)
        if (not (self.lists['_gridConvertTable'][(self.variables['pScreen'] + 4)
         - 1]
         < [10, '"0"'])

         and (self.lists['_gridConvertTable'][(self.variables['pScreen'] + 4)
         - 1]
         < [10, '"70"'])
        )
        :
            self.variables['Return value'] = self.lists['_gameGrids'][(self.lists['_gridConvertTable'][(self.variables['pScreen'] + 4)
             - 1]
             + 4)
             - 1]


        else:
            self.variables['Return value'] = [10, '"0"']




    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['_gameGrids'] = []
        self.lists['Grid._GameGrids'] = []
        self.lists['_gridConvertTable'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('_gameGrids')
            # data_showlist('Grid._GameGrids')
            # data_showlist('_gridConvertTable')
            await self.sleep(5)

        # data_hidelist('_gameGrids')
        # data_hidelist('Grid._GameGrids')
        # data_hidelist('_gridConvertTable')



    async def onbroadcast_Scratchinitialise(self, runtime):
        ("This works in the same manner as the Scratch conversion of the compact data. Grid._GameGrids holds all the arrays in a consecutive list. _gameGrids holds indexes into those array. I couldn't store the arrays as character strings because the data is modified throughout the game after being loaded (the same as the compact data is).")
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['_gameGrids'].append([10, '"0"'])

        await util.send_event_awaitable('onbroadcast_' + DatagetGridConvertTable)
        self.variables['hex'] = self.variables['Return value']
        self.variables['i'] = [10, '"0"']
        self.set_dirty(0)
        for _ in range(TIMES):
            (e, e, "1")
            self.set_dirty(0)
            if CONDITION:
                self.variables['Return value'] += 4

            self.lists['_gridConvertTable'].append(self.variables['Return value'])
            self.variables['i'] += 4

        self.variables['hex'] = [10, '""']




class skylogic(SpriteBase):
    async def onbroadcast_newLogic(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + newGrid)
        await util.send_event_awaitable('onbroadcast_' + newAutoroute)
        ()
        ()
        ()
        ()
        self.variables['_stackPtr'] = [10, '"0"']
        self.variables['_currentSection'] = [10, '"255"']
        await util.send_event_awaitable('onbroadcast_' + LogicinitScriptVariables)



    async def onbroadcast_LogicinitScreen0(self, runtime):
        ("0", "0", "0")
        self.lists['Params'].append([10, '"2"'])
        await util.send_event_awaitable('onbroadcast_' + MusicBasestartMusic)
        self.variables['_SystemVars.currentMusic'] = [10, '"2"']



    async def onbroadcast_Logicengine(self, runtime):
        self.variables['checkProtection?'] = [10, '"true"']
        self.set_dirty(0)
        while not (self.variables['checkProtection?'] == [10, '"false"'])
        :
            self.variables['temp'] = self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.LOGIC_LIST_NO'] - 1]

            self.variables['logicList'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
             + 4)
             - 1]
             + (self.variables['temp'] % 4)
            )
             - 1]

            self.variables['id'] = self.lists['SkyCompact._RawBuff'][self.variables['logicList'] - 1]

            self.variables['logicList'] += 4
            self.set_dirty(0)
            while not (self.variables['id'] == [10, '"0"'])
            :
                self.set_dirty(0)
                if (self.variables['id'] == [10, '"65535"'])
                :
                    self.variables['temp'] = self.lists['SkyCompact._RawBuff'][self.variables['logicList'] - 1]

                    self.variables['logicList'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
                     + 4)
                     - 1]
                     + (self.variables['temp'] % 4)
                    )
                     - 1]


                else:
                    self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.CUR_ID'] - 1] = self.variables['id']
                    self.variables['_compact'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['id'] / 4)
                     + 4)
                     - 1]
                     + (self.variables['id'] % 4)
                    )
                     - 1]

                    self.set_dirty(0)
                    if CONDITION:
                        self.set_dirty(0)
                        if CONDITION:
                            self.lists['Params'].append(self.variables['_compact'])
                            await util.send_event_awaitable('onbroadcast_' + GridremoveObjectFromWalk)

                        self.set_dirty(0)
                        if CONDITION:
                            self.lists['Params'].append((str([10, '"PROCESSING COMPACT# "']) + str(self.variables['id']))
                            )
                            await util.send_event_awaitable('onbroadcast_' + Debugdebug)
                            self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1]
                            )
                            await util.send_event_awaitable('onbroadcast_' + Debuglogic)

                        await util.send_event_awaitable('onbroadcast_' + self.lists['_logicTable'][(self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1]
                         + 4)
                         - 1]
                        )
                        self.set_dirty(0)
                        if CONDITION:
                            self.lists['Params'].append(self.variables['_compact'])
                            await util.send_event_awaitable('onbroadcast_' + GridobjectToWalk)

                        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                         - 1] = [10, '"0"']


                self.variables['id'] = self.lists['SkyCompact._RawBuff'][self.variables['logicList'] - 1]

                self.variables['logicList'] += 4

            ()
            self.variables['checkProtection?'] = self.variables['Return value']




    async def onbroadcast_Logicnop(self, runtime):
        pass


    async def onbroadcast_LogiclogicScript(self, runtime):
        self.set_dirty(0)
        while True:
            self.variables['_mode'] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1]

            self.lists['Params'].append(self.variables['_compact'])
            self.lists['Params'].append(self.variables['_mode'])
            await util.send_event_awaitable('onbroadcast_' + SkyCompactgetSub)
            self.variables['_scriptNo'] = self.variables['Return value']
            self.lists['Params'].append(self.variables['_compact'])
            self.lists['Params'].append((self.variables['_mode'] + 4)
            )
            await util.send_event_awaitable('onbroadcast_' + SkyCompactgetSub)
            self.variables['_offset'] = self.variables['Return value']
            (e, e)
            self.variables['_offset'] = self.variables['Return value']
            self.lists['Params'].append(self.variables['_compact'])
            self.lists['Params'].append((self.variables['_mode'] + 4)
            )
            self.lists['Params'].append(self.variables['_offset'])
            await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
            self.set_dirty(0)
            if (self.variables['_offset'] == [10, '"0"'])
            :
                self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1] = (self.variables['_mode'] - 4)


            else:
                self.set_dirty(0)
                if CONDITION:
                    return None






    async def onbroadcast_LogicautoRoute(self, runtime):
        self.lists['Params'].append(self.variables['_compact'])
        await util.send_event_awaitable('onbroadcast_' + AutorouteautoRoute)
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.variables['Return value']
        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append([10, '"1"'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactcptIsId)
        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"0"']

        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1]

            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"0"']

        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
        await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)



    async def onbroadcast_LogicarAnim(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            ()
            return None

        self.set_dirty(0)
        if CONDITION:
            ()
            return None

        self.set_dirty(0)
        if CONDITION:
            self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1]

            (e)
            self.set_dirty(0)
            if CONDITION:
                ()
                return None

            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"0"']

        self.variables['temp'] = self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.LOGIC_LIST_NO'] - 1]

        self.variables['_logicList'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
         + 4)
         - 1]
         + (self.variables['temp'] % 4)
        )
         - 1]

        self.variables['id'] = self.lists['SkyCompact._RawBuff'][self.variables['_logicList'] - 1]

        self.variables['_logicList'] += 4
        self.set_dirty(0)
        while not (self.variables['id'] == [10, '"0"'])
        :
            self.set_dirty(0)
            if (self.variables['id'] == [10, '"65535"'])
            :
                self.variables['temp'] = self.lists['SkyCompact._RawBuff'][self.variables['_logicList'] - 1]

                self.variables['_logicList'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
                 + 4)
                 - 1]
                 + (self.variables['temp'] % 4)
                )
                 - 1]


            else:
                self.set_dirty(0)
                if CONDITION:
                    self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.HIT_ID'] - 1] = self.variables['id']
                    self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['id'] / 4)
                     + 4)
                     - 1]
                     + (self.variables['id'] % 4)
                    )
                     - 1]

                    self.set_dirty(0)
                    if CONDITION:
                        self.set_dirty(0)
                        if CONDITION:
                            (e)
                            self.set_dirty(0)
                            if CONDITION:
                                self.set_dirty(0)
                                if CONDITION:
                                    self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                                     - 1] = [10, '"65535"']
                                    self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
                                     - 1] = (self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.CUR_ID'] - 1]
                                     % 4)

                                    self.lists['Params'].append(self.variables['_compact'])
                                    self.lists['Params'].append((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                                     - 1]
                                     + 4)
                                    )
                                    self.lists['Params'].append([10, '"0"'])
                                    await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
                                    self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
                                    await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)
                                    return None

                                (e, "0")
                                return None





            self.variables['id'] = self.lists['SkyCompact._RawBuff'][self.variables['_logicList'] - 1]

            self.variables['_logicList'] += 4

        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"4"']
            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1]

            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"0"']
            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"0"']
            self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
            await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)
            return None

        self.set_dirty(0)
        if CONDITION:
            ()
            return None

        self.set_dirty(0)
        if CONDITION:
            ()
            return None

        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)
        )
        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
        await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)



    async def onbroadcast_LogicarTurn(self, runtime):
        self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]

        self.variables['turnData'] = (self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
         + 4)
         - 1]
         + (self.variables['temp'] % 4)
        )
         - 1]
         + self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
        )

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.lists['SkyCompact._RawBuff'][self.variables['turnData'] - 1]

        self.variables['turnData'] += 4
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)

        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"0"']
            self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"3"']




    async def onbroadcast_Logicalt(self, runtime):
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
        )
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
        )
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)
        )
        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)



    async def onbroadcast_Logicturn(self, runtime):
        self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]

        self.variables['turnData'] = (self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
         + 4)
         - 1]
         + (self.variables['temp'] % 4)
        )
         - 1]
         + self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
        )

        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = self.lists['SkyCompact._RawBuff'][self.variables['turnData'] - 1]

            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1]
             + 4)

            return None

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"0"']
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
        await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)



    async def onbroadcast_Logiccursor(self, runtime):
        self.lists['Params'].append(self.variables['_compact'])
        await util.send_event_awaitable('onbroadcast_' + MousegiveMouseX)
        self.lists['Params'].append(self.variables['Return value'])
        await util.send_event_awaitable('onbroadcast_' + MousegiveMouseY)
        self.lists['Params'].append(self.variables['Return value'])
        await util.send_event_awaitable('onbroadcast_' + TextlogicCursor)



    async def onbroadcast_Logictalk(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + MousewasClicked)
        self.set_dirty(0)
        if CONDITION:
            self.variables['i'] = [10, '"1"']
            self.set_dirty(0)
            for _ in range(TIMES):
                self.set_dirty(0)
                if CONDITION:
                    self.set_dirty(0)
                    if CONDITION:
                        self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                         - 1]

                        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
                         + 4)
                         - 1]
                         + (self.variables['temp'] % 4)
                        )
                         - 1]

                        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
                         - 1] = [10, '"0"']
                        self.lists['Params'].append((4 - self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
                         - 1]
                        )
                        )
                        await util.send_event_awaitable('onbroadcast_' + blitdestroyText)

                    self.lists['Params'].append(self.variables['_compact'])
                    await util.send_event_awaitable('onbroadcast_' + SkyCompactgetGrafixPtr)
                    self.variables['graphixProg'] = self.variables['Return value']
                    self.set_dirty(0)
                    if CONDITION:
                        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                         - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                         - 1]

                        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                         - 1] = [10, '"0"']

                    self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
                    await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)
                    return None

                self.variables['i'] += 4


        self.lists['Params'].append(self.variables['_compact'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactgetGrafixPtr)
        self.variables['graphixProg'] = self.variables['Return value']
        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if (not (self.lists['SkyCompact._RawBuff'][self.variables['graphixProg'] - 1]
             == [10, '"0"'])

             and not (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1]
             == [10, '"3"'])

            )
            :
                self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['graphixProg'] + 4)
                 - 1]
                 + self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1]
                )

                self.variables['graphixProg'] += 4
                self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1]
                 + 4)


            else:
                self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1]

                self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1] = [10, '"0"']


        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         - 4)

        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1]

                self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
                 + 4)
                 - 1]
                 + (self.variables['temp'] % 4)
                )
                 - 1]

                self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
                 - 1] = [10, '"0"']
                self.lists['Params'].append((4 - self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
                 - 1]
                )
                )
                await util.send_event_awaitable('onbroadcast_' + blitdestroyText)

            self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
            await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)




    async def onbroadcast_Logiclisten(self, runtime):
        self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]

        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
         + 4)
         - 1]
         + (self.variables['temp'] % 4)
        )
         - 1]

        self.set_dirty(0)
        if CONDITION:
            return None

        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
        await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)



    async def onbroadcast_Logicstopped(self, runtime):
        self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]

        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
         + 4)
         - 1]
         + (self.variables['temp'] % 4)
        )
         - 1]

        self.set_dirty(0)
        if CONDITION:
            (e)
            self.set_dirty(0)
            if CONDITION:
                return None


        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         - 4)
        )
        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"65535"']
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
        await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)



    async def onbroadcast_Logicchoose(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        ()
        self.set_dirty(0)
        if CONDITION:
            self.variables['_systemVars.systemFlags'] += (4 - self.variables['SF_CHOOSING'])


        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
        await util.send_event_awaitable('onbroadcast_' + texthideBackground)
        await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)



    async def onbroadcast_Logicframes(self, runtime):
        self.set_dirty(0)
        if (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         == [10, '"0"'])
        :
            ()

        else:
            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"0"']
            self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
            await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)




    async def onbroadcast_Logicpause(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         - 4)

        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
            await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)




    async def onbroadcast_LogicwaitSync(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
            await util.send_event_awaitable('onbroadcast_' + LogiclogicScript)




    async def onbroadcast_LogicsimpleAnim(self, runtime):
        ()



    async def onbroadcast_LogicrunGetOff(self, runtime):
        self.variables['getOff'] = self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.GET_OFF'] - 1]

        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.GET_OFF'] - 1] = [10, '"0"']
        self.set_dirty(0)
        if CONDITION:
            (s, s)




    async def onbroadcast_LogiccheckModuleLoaded(self, runtime):
        self.lists['Params'].append([10, '"Logic.checkModuleLoaded"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_LogicfnExec(self, runtime):
        self.lists['Params'].append([10, '"Logic.fnExec"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_LogicinitScriptVariables(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + DatagetScriptVariables)
        self.variables['initialisationString'] = self.variables['Return value']
        self.variables['i'] = [10, '"0"']
        self.set_dirty(0)
        for _ in range(TIMES):
            (e, e, "4")
            self.lists['Logic._ScriptVariables'][((self.variables['i'] / 4)
             + 4)
             - 1] = self.variables['Return value']
            self.variables['i'] += 4

        self.variables['initialisationString'] = [10, '""']



    async def onbroadcast_LogicmouseScript(self, runtime):
        self.variables['scriptComp'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['scrNum'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['tmpComp'] = self.variables['_compact']
        self.variables['_compact'] = self.variables['scriptComp']
        (s, s)
        self.variables['retVal'] = self.variables['Return value']
        self.variables['_compact'] = self.variables['tmpComp']
        self.set_dirty(0)
        if CONDITION:
            ("0", "0", "0")

        self.variables['Return value'] = self.variables['retVal']



    async def onbroadcast_Logicscript(self, runtime):
        self.variables['offsetParam'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['scriptNoParam'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e, e)



    async def onbroadcast_LogicfnCacheChip(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + SoundfnStopFx)
        self.lists['Params'].append(self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]
        )
        await util.send_event_awaitable('onbroadcast_' + DiskfnCacheChip)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnCacheFast(self, runtime):
        self.lists['Params'].append(self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]
        )
        await util.send_event_awaitable('onbroadcast_' + DiskfnCacheFast)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnDrawScreen(self, runtime):
        self.variables['_SystemVars.currentPalette'] = self.variables['a']
        self.lists['Params'].append(self.variables['a'])
        self.lists['Params'].append(self.variables['b'])
        await util.send_event_awaitable('onbroadcast_' + ScreenfnDrawScreen)
        self.set_dirty(0)
        if CONDITION:
            await util.send_event_awaitable('onbroadcast_' + LogicfnSendSync)

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnAr(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"1"']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.variables['a']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.variables['b']
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"2"']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = ((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         / 4)

         * 4)

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = ((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         / 4)

         * 4)

        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnArAnimate(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"0"']
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"3"']
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnIdle(self, runtime):
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"0"']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnInteract(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)

        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"1"']
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
        )
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
        )
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)
        )
        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnStartSub(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)

        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
        )
        self.lists['Params'].append((self.variables['a'] % 4)
        )
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)
        )
        self.lists['Params'].append((self.variables['a'] / 4)

        )
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnTheyStartSub(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
         + 4)

        self.lists['Params'].append(self.variables['cpt'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
        )
        self.lists['Params'].append((self.variables['b'] % 4)
        )
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.lists['Params'].append(self.variables['cpt'])
        self.lists['Params'].append((self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
         + 4)
        )
        self.lists['Params'].append((self.variables['b'] / 4)

        )
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnAssignBase(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = [10, '"0"']
        self.lists['SkyCompact._RawBuff'][self.variables['cpt'] - 1] = [10, '"1"']
        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = (self.variables['b'] % 4)

        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = (self.variables['b'] / 4)


        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnDiskMouse(self, runtime):
        self.lists['Params'].append([10, '"2"'])
        self.lists['Params'].append([10, '"11"'])
        self.lists['Params'].append([10, '"11"'])
        await util.send_event_awaitable('onbroadcast_' + MousespriteMouse)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnNormalMouse(self, runtime):
        self.lists['Params'].append([10, '"1"'])
        self.lists['Params'].append([10, '"0"'])
        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + MousespriteMouse)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnBlankMouse(self, runtime):
        (e, e, e)



    async def onbroadcast_LogicfnCrossMouse(self, runtime):
        (e, e, e)



    async def onbroadcast_LogicfnCursorRight(self, runtime):
        self.lists['Params'].append([10, '"4"'])
        self.lists['Params'].append([10, '"9"'])
        self.lists['Params'].append([10, '"4"'])
        await util.send_event_awaitable('onbroadcast_' + MousespriteMouse)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnCursorLeft(self, runtime):
        self.lists['Params'].append([10, '"5"'])
        self.lists['Params'].append([10, '"0"'])
        self.lists['Params'].append([10, '"5"'])
        await util.send_event_awaitable('onbroadcast_' + MousespriteMouse)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnCursorDown(self, runtime):
        self.lists['Params'].append([10, '"3"'])
        self.lists['Params'].append([10, '"9"'])
        self.lists['Params'].append([10, '"4"'])
        await util.send_event_awaitable('onbroadcast_' + MousespriteMouse)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnCursorUp(self, runtime):
        self.lists['Params'].append([10, '"8"'])
        self.lists['Params'].append([10, '"9"'])
        self.lists['Params'].append([10, '"4"'])
        await util.send_event_awaitable('onbroadcast_' + MousespriteMouse)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnOpenHand(self, runtime):
        self.lists['Params'].append([10, '"true"'])
        await util.send_event_awaitable('onbroadcast_' + MousefnOpenCloseHand)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnCloseHand(self, runtime):
        self.lists['Params'].append([10, '"false"'])
        await util.send_event_awaitable('onbroadcast_' + MousefnOpenCloseHand)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnGetTo(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.variables['b']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)

        self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]

        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
         + 4)
         - 1]
         + (self.variables['temp'] % 4)
        )
         - 1]

        self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]

        self.variables['getToTable'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
         + 4)
         - 1]
         + (self.variables['temp'] % 4)
        )
         - 1]

        self.set_dirty(0)
        while not (self.lists['SkyCompact._RawBuff'][self.variables['getToTable'] - 1]
         == self.variables['a'])
        :
            self.variables['getToTable'] += 4

        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
        )
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['getToTable'] + 4)
         - 1]
        )
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)
        )
        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactsetSub)
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnSetToStand(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"1"']
        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append(((4 + self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
        )
         + (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         * 4)
        )
        )
        await util.send_event_awaitable('onbroadcast_' + SkyCompactgetCompactElem)
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.lists['SkyCompact._RawBuff'][self.variables['Return value'] - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"0"']
        self.lists['Params'].append(self.variables['_compact'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactgetGrafixPtr)
        self.variables['standList'] = self.variables['Return value']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.lists['SkyCompact._RawBuff'][self.variables['standList'] - 1]

        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"16"']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)

        ()
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnTurnTo(self, runtime):
        self.variables['curDir'] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.variables['a'] % 4)

        self.lists['Params'].append(self.variables['_compact'])
        self.lists['Params'].append(self.variables['curDir'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactgetTurnTable)
        self.variables['tt'] = self.variables['Return value']
        self.set_dirty(0)
        if CONDITION:
            self.variables['Return value'] = [10, '"true"']
            return None

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['tt'] + self.variables['a'])
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"0"']
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"7"']
        await util.send_event_awaitable('onbroadcast_' + Logicturn)
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnArrived(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.variables['a'] % 4)

        self.lists['Logic._ScriptVariables'][((self.variables['a'] / 4)
         + 4)
         - 1] = (self.lists['Logic._ScriptVariables'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + 4)

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnLeaving(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"0"']
        self.set_dirty(0)
        if CONDITION:
            self.lists['Logic._ScriptVariables'][((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1]
             / 4)
             + 4)
             - 1] = (self.lists['Logic._ScriptVariables'][((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1]
             / 4)
             + 4)
             - 1]
             - 4)

            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"0"']

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnSetAlternate(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.variables['a'] % 4)

        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"5"']
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnAltSetAlternate(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = (self.variables['b'] % 4)

        self.lists['SkyCompact._RawBuff'][self.variables['cpt'] - 1] = [10, '"5"']
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnKillId(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
             + 4)
             - 1]
             + (self.variables['a'] % 4)
            )
             - 1]

            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append(self.variables['cpt'])
                await util.send_event_awaitable('onbroadcast_' + GridremoveObjectFromWalk)

            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append((4 - self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
                 - 1]
                )
                )
                await util.send_event_awaitable('onbroadcast_' + blitdestroyText)

            self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
             - 1] = [10, '"0"']

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnNoHuman(self, runtime):
        ()



    async def onbroadcast_LogicfnAddHuman(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + MousefnAddHuman)



    async def onbroadcast_LogicfnAddButtons(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.MOUSE_STATUS'] - 1] = (self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.MOUSE_STATUS'] - 1]
             + 4)


        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnNoButtons(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.MOUSE_STATUS'] - 1] = (self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.MOUSE_STATUS'] - 1]
             - 4)


        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnSetStop(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.MOUSE_STOP'] - 1] = (self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.MOUSE_STOP'] - 1]
             + 4)


        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnClearStop(self, runtime):
        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.MOUSE_STOP'] - 1] = [10, '"0"']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnPointerText(self, runtime):
        self.lists['Params'].append(self.variables['a'])
        await util.send_event_awaitable('onbroadcast_' + MousegiveMouseX)
        self.lists['Params'].append(self.variables['Return value'])
        await util.send_event_awaitable('onbroadcast_' + MousegiveMouseY)
        self.lists['Params'].append(self.variables['Return value'])
        await util.send_event_awaitable('onbroadcast_' + TextfnPointerText)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnQuit(self, runtime):
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnSpeakMe(self, runtime):
        (e, e, e)



    async def onbroadcast_LogicfnSpeakMeDir(self, runtime):
        self.variables['animNum'] = self.variables['c']
        self.variables['animNum'] += (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         * 4)

        (e, e, e)



    async def onbroadcast_LogicfnSpeakWait(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.variables['a'] % 4)

        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"10"']
        await util.send_event_awaitable('onbroadcast_' + LogicfnSpeakMe)



    async def onbroadcast_LogicfnSpeakWaitDir(self, runtime):
        (e, e, e)



    async def onbroadcast_LogicfnChooser(self, runtime):
        self.lists['Params'].append(self.variables['_systemVars.systemFlags'])
        self.lists['Params'].append(self.variables['SF_CHOOSING'])
        await util.send_event_awaitable('onbroadcast_' + BitwiseOru16)
        self.variables['_systemVars.systemFlags'] = self.variables['Return value']
        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.THE_CHOSEN_ONE'] - 1] = [10, '"0"']
        self.variables['p'] = self.variables['scriptVariableOffsets.TEXT1']
        self.variables['ycood'] = [10, '"136"']
        self.set_dirty(0)
        while not (self.lists['Logic._ScriptVariables'][self.variables['p'] - 1]
         == [10, '"0"'])
        :
            self.variables['textNum'] = self.lists['Logic._ScriptVariables'][self.variables['p'] - 1]

            self.variables['p'] += 4
            self.lists['Params'].append(self.variables['textNum'])
            self.lists['Params'].append([10, '"320"'])
            self.lists['Params'].append([10, '"0"'])
            self.lists['Params'].append([10, '"241"'])
            self.lists['Params'].append([10, '"0"'])
            await util.send_event_awaitable('onbroadcast_' + TextlowTextManager)
            self.lists['Params'].append(self.variables['Return value'])
            await util.send_event_awaitable('onbroadcast_' + TextgetCompactNumFromId)
            self.variables['textCompact'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['Return value'] / 4)
             + 4)
             - 1]
             + (self.variables['Return value'] % 4)
            )
             - 1]

            self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
             - 1] = self.variables['textNum']
            self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
             - 1] = self.lists['Logic._ScriptVariables'][self.variables['p'] - 1]

            self.variables['p'] += 4
            self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
             - 1]
            )
            self.lists['Params'].append([10, '"16"'])
            await util.send_event_awaitable('onbroadcast_' + BitwiseOru16)
            self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
             - 1] = self.variables['Return value']
            self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
             - 1] = [10, '"128"']
            self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
             - 1] = self.variables['ycood']
            self.variables['ycood'] += 4
            self.lists['Params'].append((self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
             - 1]
             - 4)
            )
            self.lists['Params'].append((self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
             - 1]
             - 4)
            )
            self.lists['Params'].append((4 - self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
             - 1]
            )
            )
            await util.send_event_awaitable('onbroadcast_' + blitprepText)

        self.set_dirty(0)
        if CONDITION:
            self.variables['Return value'] = [10, '"true"']
            return None

        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"12"']
        await util.send_event_awaitable('onbroadcast_' + LogicfnAddHuman)
        self.lists['Params'].append(((self.variables['p'] - self.variables['scriptVariableOffsets.TEXT1'])
         / 4)
        )
        await util.send_event_awaitable('onbroadcast_' + textstippleBackground)
        await util.send_event_awaitable('onbroadcast_' + blitbufferedText)
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnHighlight(self, runtime):
        self.variables['pen'] = self.variables['b']
        self.variables['pen'] += 4
        self.set_dirty(0)
        if ((self.variables['pen'] % 4)
         == [10, '"0"'])
        :
            self.variables['pen'] += 4

        else:
            self.variables['pen'] += 4

        self.variables['pen'] += 4
        self.variables['textCompact'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Params'].append((self.variables['textCompact'] + 4)
        )
        await util.send_event_awaitable('onbroadcast_' + SkyEnginefetchItem)
        self.variables['sprData'] = self.variables['Return value']
        self.lists['Params'].append((4 - self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
         - 1]
        )
        )
        self.lists['Params'].append((self.variables['pen'] % 4)
        )
        await util.send_event_awaitable('onbroadcast_' + TextchangeTextSpriteColor)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnTextKill(self, runtime):
        self.variables['id'] = [10, '"23"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['id'] / 4)
             + 4)
             - 1]
             + (self.variables['id'] % 4)
            )
             - 1]

            self.set_dirty(0)
            if CONDITION:
                self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
                 - 1] = [10, '"0"']
                self.lists['Params'].append((4 - self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
                 - 1]
                )
                )
                await util.send_event_awaitable('onbroadcast_' + blitprepBufferedDestroy)

            self.variables['id'] += 4

        await util.send_event_awaitable('onbroadcast_' + blitbufferedDestroy)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnStopMode(self, runtime):
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"11"']
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnWeWait(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.variables['a']
        ()



    async def onbroadcast_LogicfnSendSync(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]
         + 4)
         - 1] = (self.variables['b'] % 4)

        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnSendFastSync(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]
         + 4)
         - 1] = (self.variables['b'] % 4)

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnSendRequest(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]
         + 4)
         - 1] = (self.variables['b'] % 4)

        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnClearRequest(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]
         + 4)
         - 1] = [10, '"0"']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnCheckRequest(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['Return value'] = [10, '"true"']
            return None

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"4"']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"0"']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"0"']
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnStartMenu(self, runtime):
        self.variables['firstObject'] = ((self.variables['a'] / 4)
         + 4)

        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][7 - 1]
         + 4)
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = [10, '"90"']
        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = (self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.SCREEN'] - 1]
         % 4)

        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][7 - 1]
         + 4)
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = [10, '"90"']
        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = (self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.SCREEN'] - 1]
         % 4)

        self.variables['menuLength'] = [10, '"0"']
        self.variables['i'] = self.variables['firstObject']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.set_dirty(0)
            if CONDITION:
                self.variables['menuLength'] += 4
                self.lists['_objectList'][self.variables['menuLength'] - 1] = self.lists['Logic._ScriptVariables'][self.variables['i'] - 1]


            self.variables['i'] += 4

        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.MENU_LENGTH'] - 1] = self.variables['menuLength']
        self.variables['blankID'] = [10, '"51"']
        self.variables['i'] = self.variables['menuLength']
        self.set_dirty(0)
        while not (self.variables['i'] > [10, '"10"'])
        :
            self.lists['_objectList'][(self.variables['i'] + 4)
             - 1] = self.variables['blankID']
            self.variables['blankID'] += 4
            self.variables['i'] += 4

        self.variables['break?'] = [10, '"false"']
        self.variables['i'] = [10, '"0"']
        self.set_dirty(0)
        while not ((self.variables['i'] == [10, '"30"'])
         or (self.variables['break?'] == [10, '"true"'])
        )
        :
            self.set_dirty(0)
            if not (self.lists['_objectList'][(self.variables['i'] + 4)
             - 1]
             == [10, '"0"'])

            :
                self.variables['temp'] = self.lists['_objectList'][(self.variables['i'] + 4)
                 - 1]

                self.lists['SkyCompact._RawBuff'][(self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
                 + 4)
                 - 1]
                 + (self.variables['temp'] % 4)
                )
                 - 1]
                 + 4)
                 - 1] = [10, '"64"']
                self.variables['i'] += 4

            else:
                self.variables['break?'] = [10, '"true"']


        self.set_dirty(0)
        if (self.variables['menuLength'] < [10, '"11"'])
        :
            self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.SCROLL_OFFSET'] - 1] = [10, '"0"']

        else:
            self.set_dirty(0)
            if CONDITION:
                self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.SCROLL_OFFSET'] - 1] = (self.variables['menuLength'] - 4)



        self.variables['rollingX'] = [10, '"156"']
        self.variables['i'] = [10, '"0"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.variables['temp'] = self.lists['_objectList'][((self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.SCROLL_OFFSET'] - 1]
             + self.variables['i'])
             + 4)
             - 1]

            self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
             + 4)
             - 1]
             + (self.variables['temp'] % 4)
            )
             - 1]

            self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
             - 1] = [10, '"90"']
            self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
             - 1] = (self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.SCREEN'] - 1]
             % 4)

            self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
             - 1] = self.variables['rollingX']
            self.variables['rollingX'] += 4
            self.set_dirty(0)
            if (self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.MENU'] - 1]
             == [10, '"2"'])
            :
                self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
                 - 1] = [10, '"136"']

            else:
                self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
                 - 1] = [10, '"112"']

            self.variables['i'] += 4

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnFaceId(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.variables['x'] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         - self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
        )

        (e)
        self.variables['x'] = self.variables['Return value']
        self.set_dirty(0)
        if (self.variables['x'] < [10, '"0"'])
        :
            self.variables['x'] = (4 - self.variables['x'])

            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"3"']

        else:
            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = [10, '"2"']

        self.variables['y'] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         - (self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
         + (self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
         + self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
        )
        )
        )

        (e)
        self.variables['y'] = self.variables['Return value']
        self.set_dirty(0)
        if (self.variables['y'] < [10, '"0"'])
        :
            self.variables['y'] = (4 - self.variables['y'])

            self.set_dirty(0)
            if CONDITION:
                self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1] = [10, '"1"']


        else:
            self.set_dirty(0)
            if CONDITION:
                self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
                 - 1] = [10, '"0"']


        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnForeground(self, runtime):
        self.variables['temp'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
         - 1] = ((self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
         - 1]
         / 4)

         * 4)

        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
             - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
             - 1]
             + 4)


        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnBackground(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = ((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         / 4)

         * 4)

        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
             - 1]
             + 4)


        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnNewBackground(self, runtime):
        self.variables['temp'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
         - 1] = ((self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
         - 1]
         / 4)

         * 4)

        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
             - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
             - 1]
             + 4)


        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnSort(self, runtime):
        self.variables['temp'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
         - 1] = ((self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
         - 1]
         / 4)

         * 4)

        self.set_dirty(0)
        if CONDITION:
            self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
             - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
             - 1]
             + 4)


        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnNoSpriteEngine(self, runtime):
        self.lists['_logicTable'][(self.variables['_compact'] + 4)
         - 1] = ((self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         / 4)

         * 4)

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnNoSpritesA6(self, runtime):
        self.variables['temp'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
         - 1] = ((self.lists['SkyCompact._RawBuff'][(self.variables['temp'] + 4)
         - 1]
         / 4)

         * 4)

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnResetId(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.variables['rst'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['b'] / 4)
         + 4)
         - 1]
         + (self.variables['b'] % 4)
        )
         - 1]

        self.set_dirty(0)
        while True:
            self.variables['off'] = self.lists['SkyCompact._RawBuff'][self.variables['rst'] - 1]

            self.variables['rst'] += 4
            self.set_dirty(0)
            if CONDITION:
                self.variables['Return value'] = [10, '"true"']
                return None

            self.lists['Params'].append(self.variables['cpt'])
            self.lists['Params'].append(self.variables['off'])
            await util.send_event_awaitable('onbroadcast_' + SkyCompactgetCompactElem)
            self.lists['SkyCompact._RawBuff'][self.variables['Return value'] - 1] = self.lists['SkyCompact._RawBuff'][self.variables['rst'] - 1]

            self.variables['rst'] += 4




    async def onbroadcast_LogicfnToggleGrid(self, runtime):
        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
        )
        self.lists['Params'].append([10, '"128"'])
        await util.send_event_awaitable('onbroadcast_' + BitwiseXORu16)
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.variables['Return value']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnPause(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.variables['a'] % 4)

        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"14"']
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnRunAnimMod(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.variables['a']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"0"']
        self.lists['Params'].append(self.variables['_compact'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactgetGrafixPtr)
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.lists['SkyCompact._RawBuff'][self.variables['Return value'] - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)

        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"6"']
        ()
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnSimpleMod(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.variables['a']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"0"']
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"16"']
        self.lists['Params'].append(self.variables['_compact'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactgetGrafixPtr)
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.lists['SkyCompact._RawBuff'][self.variables['Return value'] - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)

        ()
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnRunFrames(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.variables['a']
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = [10, '"0"']
        self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"13"']
        self.lists['Params'].append(self.variables['_compact'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactgetGrafixPtr)
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = self.lists['SkyCompact._RawBuff'][self.variables['Return value'] - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)

        ()
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnAwaitSync(self, runtime):
        self.set_dirty(0)
        if not (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         == [10, '"0"'])

        :
            self.variables['Return value'] = [10, '"true"']

        else:
            self.lists['SkyCompact._RawBuff'][self.variables['_compact'] - 1] = [10, '"15"']
            self.variables['Return value'] = [10, '"false"']




    async def onbroadcast_LogicfnIncMegaSet(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         + 4)

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnDecMegaSet(self, runtime):
        self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['_compact'] + 4)
         - 1]
         - 4)

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnSetMegaSet(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = (self.variables['b'] * 4)

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnMoveItems(self, runtime):
        self.variables['temp'] = self.lists['SkyCompact._RawBuff'][(self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][7 - 1]
         + 4)
         - 1]
         + self.variables['a'])
         - 1]

        self.variables['p'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
         + 4)
         - 1]
         + (self.variables['temp'] % 4)
        )
         - 1]

        self.set_dirty(0)
        for _ in range(TIMES):
            self.set_dirty(0)
            if CONDITION:
                self.variables['Return value'] = [10, '"true"']
                return None

            self.variables['temp'] = self.lists['SkyCompact._RawBuff'][self.variables['p'] - 1]

            self.variables['p'] += 4
            self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['temp'] / 4)
             + 4)
             - 1]
             + (self.variables['temp'] % 4)
            )
             - 1]

            self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
             - 1] = (self.variables['b'] % 4)

            self.variables['Return value'] = [10, '"true"']

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnNewList(self, runtime):
        self.variables['i'] = [10, '"0"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['Logic._ScriptVariables'][(self.variables['scriptVariableOffsets.TEXT1'] + self.variables['i'])
             - 1] = [10, '"0"']
            self.variables['i'] += 4

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnAskThis(self, runtime):
        self.variables['p'] = self.variables['scriptVariableOffsets.TEXT1']
        self.set_dirty(0)
        while not (self.lists['Logic._ScriptVariables'][self.variables['p'] - 1]
         == [10, '"0"'])
        :
            self.variables['p'] += 4

        self.lists['Logic._ScriptVariables'][self.variables['p'] - 1] = self.variables['a']
        self.variables['p'] += 4
        self.lists['Logic._ScriptVariables'][self.variables['p'] - 1] = self.variables['b']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnRandom(self, runtime):
        self.lists['Params'].append(random.randint(4, 4)
        )
        self.lists['Params'].append(self.variables['a'])
        await util.send_event_awaitable('onbroadcast_' + BitwiseAndu16)
        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.RND'] - 1] = self.variables['Return value']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnPersonHere(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.RESULT'] - 1] = ((self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
         == self.variables['b'])
         * 4)

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnToggleMouse(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
        )
        self.lists['Params'].append([10, '"16"'])
        await util.send_event_awaitable('onbroadcast_' + BitwiseXORu16)
        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = self.variables['Return value']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnMouseOn(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
        )
        self.lists['Params'].append([10, '"16"'])
        await util.send_event_awaitable('onbroadcast_' + BitwiseOru16)
        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = self.variables['Return value']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnMouseOff(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Params'].append(self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
        )
        self.lists['Params'].append((4 - 4)
        )
        await util.send_event_awaitable('onbroadcast_' + BitwiseAndu16)
        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = self.variables['Return value']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnFetchX(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.RESULT'] - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnFetchY(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.RESULT'] - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnTestList(self, runtime):
        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.RESULT'] - 1] = [10, '"0"']
        self.variables['list'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.set_dirty(0)
        while not (self.lists['SkyCompact._RawBuff'][self.variables['list'] - 1]
         == [10, '"0"'])
        :
            self.set_dirty(0)
            if CONDITION:
                self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.RESULT'] - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['list'] + 4)
                 - 1]


            self.variables['list'] += 4

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnFetchPlace(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.RESULT'] - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnCustomJoey(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.PLAYER_X'] - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]

        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.PLAYER_Y'] - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]

        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.PLAYER_MOOD'] - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]

        self.lists['Logic._ScriptVariables'][self.variables['scriptVariableOffsets.PLAYER_SCREEN'] - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnSetPalette(self, runtime):
        self.lists['Params'].append([10, '"Logic.fnSetPalette"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_LogicfnTextModule(self, runtime):
        self.lists['Params'].append(self.variables['a'])
        self.lists['Params'].append(self.variables['b'])
        await util.send_event_awaitable('onbroadcast_' + TextfnTextModule)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnChangeName(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['Logic._ScriptVariables'][(self.variables['cpt'] + 4)
         - 1] = self.variables['b']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnMiniLoad(self, runtime):
        self.lists['Params'].append(self.variables['a'])
        await util.send_event_awaitable('onbroadcast_' + DiskfnMiniLoad)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnFlushBuffers(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + DiskfnFlushBuffers)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnFlushChip(self, runtime):
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnSaveCoods(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + MousefnSaveCoods)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnPlotGrid(self, runtime):
        self.lists['Params'].append(self.variables['a'])
        self.lists['Params'].append(self.variables['b'])
        self.lists['Params'].append(self.variables['c'])
        self.lists['Params'].append(self.variables['_compact'])
        await util.send_event_awaitable('onbroadcast_' + GridplotGrid)



    async def onbroadcast_LogicfnRemoveGrid(self, runtime):
        self.lists['Params'].append(self.variables['a'])
        self.lists['Params'].append(self.variables['b'])
        self.lists['Params'].append(self.variables['c'])
        self.lists['Params'].append(self.variables['_compact'])
        await util.send_event_awaitable('onbroadcast_' + GridremoveGrid)



    async def onbroadcast_LogicfnEyeball(self, runtime):
        self.lists['Params'].append([10, '"Logic.fnEyeball"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_LogicfnRestoreGame(self, runtime):
        self.lists['Params'].append([10, '"Logic.fnRestoreGame"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_LogicfnRestartGame(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + ControlrestartGame)
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_LogicfnNewSwingSeq(self, runtime):
        self.set_dirty(0)
        if (((self.variables['a'] == [10, '"85"'])
         or (self.variables['a'] == [10, '"106"'])
        )
         or ((self.variables['a'] == [10, '"75"'])
         or (self.variables['a'] == [10, '"15"'])
        )
        )
        :
            self.lists['Params'].append(self.variables['a'])
            await util.send_event_awaitable('onbroadcast_' + ScreenstartSequenceItem)

        else:

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnWaitSwingEnd(self, runtime):
        self.lists['Params'].append([10, '"Logic.fnWaitSwingEnd"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_LogicfnSkipIntroCode(self, runtime):
        self.variables['_SystemVars.pastIntro'] = [10, '"true"']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnBlankScreen(self, runtime):
        self.lists['Params'].append([10, '"Logic.fnBlankScreen"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_LogicfnPrintCredit(self, runtime):
        self.lists['Params'].append([10, '"Logic.fnPrintCredit"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_LogicfnLookAt(self, runtime):
        self.lists['Params'].append(self.variables['a'])
        self.lists['Params'].append([10, '"240"'])
        self.lists['Params'].append([10, '"0"'])
        self.lists['Params'].append([10, '"248"'])
        self.lists['Params'].append([10, '"true"'])
        await util.send_event_awaitable('onbroadcast_' + TextlowTextManager)
        self.variables['textInfo'] = self.variables['Return value']
        self.lists['Params'].append(self.variables['Return value'])
        await util.send_event_awaitable('onbroadcast_' + TextgetCompactNumFromId)
        self.variables['textCpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['Return value'] / 4)
         + 4)
         - 1]
         + (self.variables['Return value'] % 4)
        )
         - 1]

        self.lists['Params'].append((4 - 4)
        )
        self.lists['Params'].append((self.variables['c'] - 4)
        )
        self.lists['Params'].append((4 - self.lists['SkyCompact._RawBuff'][(self.variables['textCpt'] + 4)
         - 1]
        )
        )
        await util.send_event_awaitable('onbroadcast_' + blittext)
        await util.send_event_awaitable('onbroadcast_' + Screenrecreate)
        await util.send_event_awaitable('onbroadcast_' + ScreenspriteEngine)
        self.lists['Params'].append([10, '"true"'])
        await util.send_event_awaitable('onbroadcast_' + Screenflip)
        ()
        await util.send_event_awaitable('onbroadcast_' + MouselockMouse)
        self.lists['Params'].append([10, '"800"'])
        await util.send_event_awaitable('onbroadcast_' + MousewaitMouseNotPressed)
        await util.send_event_awaitable('onbroadcast_' + MouseunlockMouse)
        await util.send_event_awaitable('onbroadcast_' + LogicfnAddHuman)
        self.lists['SkyCompact._RawBuff'][(self.variables['textCpt'] + 4)
         - 1] = [10, '"0"']
        self.lists['Params'].append((4 - self.lists['SkyCompact._RawBuff'][(self.variables['textCpt'] + 4)
         - 1]
        )
        )
        await util.send_event_awaitable('onbroadcast_' + blitdestroyText)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnLincTextModule(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['cnt'] = self.variables['scriptVariableOffsets.LINC_DIGIT_0']
            self.set_dirty(0)
            for _ in range(TIMES):
                self.lists['Logic._ScriptVariables'][self.variables['cnt'] - 1] = [10, '"0"']
                self.variables['cnt'] += 4


        self.variables['buttonAction'] = (self.variables['c'] % 4)

        self.set_dirty(0)
        if CONDITION:
            self.lists['Logic._ScriptVariables'][(self.variables['scriptVariableOffsets.LINC_DIGIT_0'] + self.variables['buttonAction'])
             - 1] = self.variables['b']

        self.lists['Params'].append(self.variables['b'])
        self.lists['Params'].append([10, '"220"'])
        self.lists['Params'].append([10, '"0"'])
        self.lists['Params'].append([10, '"215"'])
        self.lists['Params'].append([10, '"false"'])
        await util.send_event_awaitable('onbroadcast_' + TextlowTextManager)
        self.lists['Params'].append(self.variables['Return value'])
        await util.send_event_awaitable('onbroadcast_' + TextgetCompactNumFromId)
        self.variables['textCompact'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['Return value'] / 4)
         + 4)
         - 1]
         + (self.variables['Return value'] % 4)
        )
         - 1]

        self.set_dirty(0)
        if (self.variables['a'] < [10, '"20"'])
        :
            self.variables['xPos'] = [10, '"152"']
            self.variables['yPos'] = ((self.variables['a'] * 4)
             + 4)


        else:
            self.set_dirty(0)
            if CONDITION:
                self.variables['xPos'] = self.variables['a']
                self.variables['yPos'] = [10, '"214"']


        self.lists['Params'].append((self.variables['xPos'] - 4)
        )
        self.lists['Params'].append((self.variables['yPos'] - 4)
        )
        self.lists['Params'].append((4 - self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
         - 1]
        )
        )
        await util.send_event_awaitable('onbroadcast_' + blittext)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnTextKill2(self, runtime):
        self.variables['id'] = [10, '"23"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['id'] / 4)
             + 4)
             - 1]
             + (self.variables['id'] % 4)
            )
             - 1]

            self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
             - 1] = [10, '"0"']
            self.lists['Params'].append((4 - self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
             - 1]
            )
            )
            await util.send_event_awaitable('onbroadcast_' + blitprepBufferedDestroy)
            self.variables['id'] += 4

        await util.send_event_awaitable('onbroadcast_' + blitbufferedDestroy)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnSetFont(self, runtime):
        self.lists['Params'].append(self.variables['a'])
        await util.send_event_awaitable('onbroadcast_' + TextfnSetFont)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnStartFx(self, runtime):
        (e, e, e)



    async def onbroadcast_LogicfnStopFx(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + SoundfnStopFx)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnStartMusic(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append(self.variables['a'])
            await util.send_event_awaitable('onbroadcast_' + MusicBasestartMusic)

        self.variables['_SystemVars.currentMusic'] = self.variables['a']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnStopMusic(self, runtime):
        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + MusicBasestopMusic)
        self.variables['_SystemVars.currentMusic'] = [10, '"0"']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnFadeDown(self, runtime):
        self.lists['Params'].append([10, '"Logic.fnFadeDown"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnFadeUp(self, runtime):
        self.lists['Params'].append([10, '"Logic.fnFadeUp"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnQuitToDos(self, runtime):
        self.lists['Params'].append([10, '"Logic.fnQuitToDos"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnPauseFx(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + SoundfnPauseFx)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnUnPauseFx(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + SoundfnUnPauseFx)
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicfnPrintf(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append((str((str((str((str((str((str([10, '"fnPrintf("']) + str(self.variables['a']))
            ) + str([10, '", "']))
            ) + str(self.variables['b']))
            ) + str([10, '", "']))
            ) + str(self.variables['c']))
            ) + str([10, '")"']))
            )
            await util.send_event_awaitable('onbroadcast_' + Debugdebug)




    async def onbroadcast_LogicuseControlInstance(self, runtime):
        ("Unneeded because there is only one control instance")



    async def onbroadcast_Scratchinitialise(self, runtime):
        ()



    async def onbroadcast_Scratchreset(self, runtime):
        self.variables['data'] = [10, '""']
        self.variables['scriptData'] = [10, '"0"']
        self.lists['_objectList'] = []
        self.lists['Logic._ScriptVariables'] = []
        self.lists['_logicTable'] = []
        self.lists['_moduleList'] = []
        self.lists['_mcodeTable'] = []
        self.lists['_stack'] = []
        self.lists['script locals stack'] = []
        self.lists['allScriptData'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showvariable('data')
            # data_showvariable('scriptData')
            # data_showlist('_objectList')
            # data_showlist('Logic._ScriptVariables')
            # data_showlist('_logicTable')
            # data_showlist('_moduleList')
            # data_showlist('_mcodeTable')
            # data_showlist('_stack')
            # data_showlist('script locals stack')
            # data_showlist('allScriptData')
            await self.sleep(5)

        # data_hidevariable('data')
        # data_hidevariable('scriptData')
        # data_hidelist('_objectList')
        # data_hidelist('Logic._ScriptVariables')
        # data_hidelist('_logicTable')
        # data_hidelist('_moduleList')
        # data_hidelist('_mcodeTable')
        # data_hidelist('_stack')
        # data_hidelist('script locals stack')
        # data_hidelist('allScriptData')



    async def onbroadcast_Logicanim(self, runtime):
        ()



    async def onbroadcast_LogicfnUnhighlight(self, runtime):
        self.variables['cpt'] = self.lists['SkyCompact._Compacts'][(self.lists['SkyCompact._DataOffsets'][((self.variables['a'] / 4)
         + 4)
         - 1]
         + (self.variables['a'] % 4)
        )
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = (self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1]
         - 4)

        self.lists['SkyCompact._RawBuff'][(self.variables['cpt'] + 4)
         - 1] = [10, '"0"']
        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_LogicparseSaveData(self, runtime):
        self.variables['dataIndex'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e, "0", "0")
        self.variables['cnt'] = [10, '"1"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['Logic._ScriptVariables'][self.variables['cnt'] - 1] = (self.lists['SaveGameData'][self.variables['dataIndex'] - 1]
             + (self.lists['SaveGameData'][(self.variables['dataIndex'] + 4)
             - 1]
             * 4)
            )

            self.variables['cnt'] += 4
            self.variables['dataIndex'] += 4

        (e, "0", "0")




class skymouse(SpriteBase):
    async def onbroadcast_newMouse(self, runtime):
        self.variables['_mouseB'] = [10, '"0"']
        self.variables['_currentCursor'] = [10, '"6"']
        self.variables['_mouseX'] = [10, '"160"']
        self.variables['_mouseY'] = [10, '"96"']
        self.lists['Params'].append([10, '"60300"'])
        await util.send_event_awaitable('onbroadcast_' + DiskloadFile)
        self.variables['_miceData'] = self.variables['Return value']
        self.lists['Params'].append([10, '"60301"'])
        await util.send_event_awaitable('onbroadcast_' + DiskloadFile)
        self.variables['_objectMouseData'] = self.variables['Return value']
        self.variables['_heldObject'] = [10, '"0"']
        self.variables['mouseUp?'] = [10, '"false"']



    async def onbroadcast_MousereplaceMouseCursors(self, runtime):
        self.variables['fileNo'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].append(self.variables['fileNo'])
        await util.send_event_awaitable('onbroadcast_' + DiskloadFile)
        self.variables['_objectMouseData'] = self.variables['Return value']



    async def onbroadcast_MousefnAddHuman(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append(self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.MOUSE_STATUS']
             - 1]
            )
            self.lists['Params'].append([10, '"6"'])
            await util.send_event_awaitable('onbroadcast_' + BitwiseOru16)
            self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.MOUSE_STATUS']
             - 1] = self.variables['Return value']
            self.set_dirty(0)
            if CONDITION:
                self.variables['_mouseY'] = [10, '"2"']

            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append((self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.GET_OFF']
                 - 1]
                 % 4)
                )
                self.lists['Params'].append((self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.GET_OFF']
                 - 1]
                 / 4)

                )
                await util.send_event_awaitable('onbroadcast_' + Logicscript)

            self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.SPECIAL_ITEM']
             - 1] = [10, '"4294967295"']
            self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.GET_OFF']
             - 1] = [10, '"23"']

        self.variables['Return value'] = [10, '"true"']



    async def onbroadcast_MousefnSaveCoods(self, runtime):
        self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.SAFE_X']
         - 1] = (self.variables['_mouseX'] + 4)

        self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.SAFE_Y']
         - 1] = (self.variables['_mouseY'] + self.variables['TOP_LEFT_Y'])




    async def onbroadcast_MouselockMouse(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['_systemVars.systemFlags'] += self.variables['SF_MOUSE_LOCKED']




    async def onbroadcast_MouseunlockMouse(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['_systemVars.systemFlags'] += (4 - self.variables['SF_MOUSE_LOCKED'])





    async def onbroadcast_MouserestoreMouseData(self, runtime):
        pass


    async def onbroadcast_MousedrawNewMouse(self, runtime):
        pass


    async def onbroadcast_MousewaitMouseNotPressed(self, runtime):
        self.variables['minDelay'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['mousePressed'] = [10, '"true"']
        await util.send_event_awaitable('onbroadcast_' + scratchgetMillis)
        self.variables['now'] = self.variables['Return value']
        self.set_dirty(0)
        while not not ((self.variables['mousePressed'] == [10, '"true"'])
         or (self.variables['Return value'] < (self.variables['now'] + self.variables['minDelay'])
        )
        )

        :
            self.variables['mousePressed'] = pg.mouse.get_pressed()[0]

            self.set_dirty(0)
            if CONDITION:
                self.variables['minDelay'] = [10, '"0"']
                self.variables['mousePressed'] = [10, '"false"']

            await util.send_event_awaitable('onbroadcast_' + scratchgetMillis)




    async def onbroadcast_MousespriteMouse(self, runtime):
        self.variables['mouseY'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['mouseX'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['frameNum'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['_currentCursor'] = self.variables['frameNum']
        (e, "6", "2")
        self.variables['mouseWidth'] = self.variables['Return value']
        (e, "8", "2")
        self.variables['mouseHeight'] = self.variables['Return value']
        self.variables['hotspotX'] = self.variables['mouseX']
        self.variables['hotspotY'] = self.variables['mouseY']
        self.set_dirty(0)
        if CONDITION:
            self.variables['_heldObject'] = [10, '"0"']




    async def onbroadcast_MousemouseEngine(self, runtime):
        self.variables['_logicClick'] = (self.variables['_mouseB'] > [10, '"0"'])

        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                (s, s)
                self.set_dirty(0)
                if CONDITION:
                    ()



        self.variables['_mouseB'] = [10, '"0"']



    async def onbroadcast_MousebuttonPressed(self, runtime):
        self.lists['Params'].append([10, '"Mouse.buttonPressed should not be called"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_MousemouseMoved(self, runtime):
        self.lists['Params'].append([10, '"Mouse.mouseMoved should not be called"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_MouseresetCursor(self, runtime):
        self.lists['Params'].append(self.variables['_currentCursor'])
        self.lists['Params'].append([10, '"0"'])
        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + MousespriteMouse)



    async def onbroadcast_MousefindMouseCursor(self, runtime):
        self.variables['itemNum'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['cnt'] = [10, '"0"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.set_dirty(0)
            if CONDITION:
                self.variables['Return value'] = self.variables['cnt']
                return None

            self.variables['cnt'] += 4

        self.variables['cnt'] = [10, '"0"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.set_dirty(0)
            if CONDITION:
                self.variables['Return value'] = self.variables['cnt']
                return None

            self.variables['cnt'] += 4

        self.variables['Return value'] = [10, '"0"']



    async def onbroadcast_MousefnOpenCloseHand(self, runtime):
        self.variables['open'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.set_dirty(0)
        if CONDITION:
            self.variables['_heldObject'] = [10, '"0"']
            self.lists['Params'].append([10, '"1"'])
            self.lists['Params'].append([10, '"0"'])
            self.lists['Params'].append([10, '"0"'])
            await util.send_event_awaitable('onbroadcast_' + MousespriteMouse)
            return None

        self.lists['Params'].append(self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.OBJECT_HELD']
         - 1]
        )
        await util.send_event_awaitable('onbroadcast_' + MousefindMouseCursor)
        self.variables['cursor'] = (self.variables['Return value'] * 4)

        self.set_dirty(0)
        if CONDITION:
            self.variables['cursor'] += 4

        self.variables['_heldObject'] = self.variables['cursor']
        self.lists['Params'].append([10, '"0"'])
        self.lists['Params'].append([10, '"5"'])
        self.lists['Params'].append([10, '"5"'])
        await util.send_event_awaitable('onbroadcast_' + MousespriteMouse)



    async def onbroadcast_MousewasClicked(self, runtime):
        self.set_dirty(0)
        if (self.variables['_logicClick'] == [10, '"true"'])
        :
            self.variables['_logicClick'] = [10, '"false"']
            self.variables['Return value'] = [10, '"true"']

        else:
            self.variables['Return value'] = [10, '"false"']




    async def onbroadcast_MouseuseLogicInstance(self, runtime):
        pass


    async def onbroadcast_MousegiveMouseX(self, runtime):
        self.variables['Return value'] = self.variables['_mouseX']



    async def onbroadcast_MousegiveMouseY(self, runtime):
        self.variables['Return value'] = self.variables['_mouseY']



    async def onbroadcast_MousegiveCurrentMouseType(self, runtime):
        self.variables['Return value'] = self.variables['_currentCursor']



    async def onbroadcast_MouselogicClick(self, runtime):
        self.variables['_logicClick'] = [10, '"true"']



    async def onbroadcast_Scratchreset(self, runtime):
        self.variables['_miceData'] = [10, '""']
        self.variables['_objectMouseData'] = [10, '""']
        self.variables['frameNum'] = [10, '"0"']
        self.visible = 0



    async def onbroadcast__blitmouse(self, runtime):
        self.size = (self.variables['Scale'] * 4)

        self.set_dirty(0)
        if (self.variables['_heldObject'] > [10, '"0"'])
        :
            self.costume = self.get_costume((str((str([10, '"60301"']) + str([10, '"_"']))
            ) + str(self.variables['_heldObject']))
            )
            self.xpos = ((((self.variables['_mouseX'] - 4)
             + (self.variables['mouseWidth'] / 4)
            )
             - 4)
             * self.variables['Scale'])

            self.ypos = (4 + ((((4 - self.variables['_mouseY'])
             - (self.variables['mouseHeight'] / 4)
            )
             + 4)
             * self.variables['Scale'])
            )


        else:
            self.costume = self.get_costume((str((str([10, '"60300"']) + str([10, '"_"']))
            ) + str(self.variables['frameNum']))
            )
            self.xpos = ((((self.variables['_mouseX'] - 4)
             + (self.variables['mouseWidth'] / 4)
            )
             - self.variables['hotspotX'])
             * self.variables['Scale'])

            self.ypos = (4 + ((((4 - self.variables['_mouseY'])
             - (self.variables['mouseHeight'] / 4)
            )
             + self.variables['hotspotY'])
             * self.variables['Scale'])
            )


        self.set_dirty(0)
        if ((self.variables['frameNum'] == [10, '"6"'])
         or ([10, '"-108"'] > pg.mouse.get_pos()[1]
        )
        )
        :
            self.visible = 0

        else:
            self.visible = 1




    async def onbroadcast__mouseupdateMouse(self, runtime):
        self.variables['_mouseX'] = ((pg.mouse.get_pos()[0]
         / self.variables['Scale'])
         + 4)

        self.variables['_mouseY'] = (4 - ((pg.mouse.get_pos()[1]
         + 4)
         / self.variables['Scale'])
        )

        self.set_dirty(0)
        if (self.variables['_mouseX'] < [10, '"0"'])
        :
            self.variables['_mouseX'] = [10, '"0"']

        else:
            self.set_dirty(0)
            if CONDITION:
                self.variables['_mouseX'] = [10, '"320"']


        self.set_dirty(0)
        if (self.variables['_mouseY'] < [10, '"4"'])
        :
            self.variables['_mouseY'] = [10, '"4"']

        else:
            self.set_dirty(0)
            if CONDITION:
                self.variables['_mouseY'] = [10, '"192"']


        self.set_dirty(0)
        if pg.mouse.get_pressed()[0]
        :
            self.set_dirty(0)
            if CONDITION:
                self.variables['_mouseB'] = (4 + (self.variables['Toolbar.useActive?'] == [10, '"false"'])
                )

                self.variables['mouseUp?'] = [10, '"false"']


        else:
            self.variables['mouseUp?'] = [10, '"true"']





class skymusicbase(SpriteBase):
    async def onbroadcast_newMusicBase(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['_currentMusic'] = [10, '"0"']
            self.variables['_musicVolume'] = [10, '"50"']
            self.variables['_currentMusic'] = [10, '"0"']
            self.variables['MusicBase.IsPlaying?'] = [10, '"false"']




    async def onbroadcast_deleteMusicBase(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"delete MusicBase"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def onbroadcast_MusicBaseloadSection(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['pSection'] = self.lists['Params'][len(self.lists['Params'])
             - 1]

            self.lists['Params'].pop(len(self.lists['Params'])
             - 1)
            self.variables['_currentSection'] = self.variables['pSection']
            self.variables['_onNextPoll.musicToProcess'] = [10, '"0"']




    async def onbroadcast_MusicBasemusicIsPlaying(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['Return value'] = self.variables['MusicBase.IsPlaying?']




    async def onbroadcast_MusicBasestartMusic(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['param'] = self.lists['Params'][len(self.lists['Params'])
             - 1]

            self.lists['Params'].pop(len(self.lists['Params'])
             - 1)
            self.variables['_onNextPoll.musicToProcess'] = (self.variables['param'] % 4)

            ()




    async def onbroadcast_MusicBasestopMusic(self, runtime):
        self.set_dirty(0)
        if (self.variables['clone?'] == [10, '"true"'])
        :
            # control_delete_this_clone()

        else:
            self.variables['MusicBase.IsPlaying?'] = [10, '"false"']




    async def onbroadcast_MusicBasegiveVolume(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"MusicBase.giveVolume"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def onbroadcast_MusicBasegiveCurrentMusic(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['Return value'] = self.variables['_currentMusic']




    async def onbroadcast_MusicBasesetVolume(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"MusicBase.setVolume"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def onbroadcast_MusicBaseupdateTempo(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"MusicBase.updateTempo"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def clone_start(self, runtime):
        self.variables['clone?'] = [10, '"true"']
        self.variables['MusicBase.IsPlaying?'] = [10, '"true"']
        # sound_setvolumeto((self.variables['_musicVolume'] * ((self.variables['_systemVars.systemFlags'] % (self.variables['SF_MUS_OFF'] * 4)
        )
         < self.variables['SF_MUS_OFF'])
        )
        )
        self.set_dirty(0)
        while True:
            # sound_playuntildone((str((str([10, '"music_"']) + str(self.variables['section']))
            ) + str(self.variables['song']))
            )
            self.set_dirty(0)
            if CONDITION:
                self.variables['MusicBase.IsPlaying?'] = [10, '"false"']
                return None





    async def onbroadcast_Scratchinitialise(self, runtime):
        self.variables['clone?'] = [10, '"false"']



    async def onbroadcast_MusicsetEnabled(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            # sound_setvolumeto((self.variables['_musicVolume'] * ((self.variables['_systemVars.systemFlags'] % (self.variables['SF_MUS_OFF'] * 4)
            )
             < self.variables['SF_MUS_OFF'])
            )
            )





class skyscreen(SpriteBase):
    async def onbroadcast_newScreen(self, runtime):
        self.variables['_seqInfo.nextFrame'] = [10, '"0"']
        self.variables['_seqInfo.framesLeft'] = [10, '"0"']
        self.variables['_seqInfo.running'] = [10, '"false"']



    async def onbroadcast_ScreenclearScreen(self, runtime):
        self.variables['fullscreen'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        # pen_clear()



    async def onbroadcast_ScreensetFocusRectangle(self, runtime):
        self.lists['Params'].append([10, '"Screen.setFocusRectangle"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ScreensetPaletteuint8(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"Screen.setPalette (uint8*): Serves no purpose"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def onbroadcast_ScreensetPaletteEndian(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"Screen.setPaletteEndian: Serves no purpose"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def onbroadcast_ScreenhalvePalette(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"Screen.halvePalette: Serves no purpose"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def onbroadcast_ScreensetPaletteuint16(self, runtime):
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"Screen.setPalette (uint16): Serves no purpose"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def onbroadcast_ScreenshowScreenuinty16bool(self, runtime):
        self.variables['fullscreen'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['filenum'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['_blit.backdrop'] = self.variables['filenum']
        await util.send_event_awaitable('onbroadcast_' + blitbackground)



    async def onbroadcast_ScreenshowScreenuint8bool(self, runtime):
        self.lists['Params'].append([10, '"Screen.showScreen (uint8*, bool)"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_Screenrecreate(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.variables['_blit.backdrop'] = [10, '"-1"']
        self.variables['temp'] = self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.LAYER_0_ID']
         - 1]

        self.variables['i'] = [10, '"1"']
        self.set_dirty(0)
        while not (self.lists['SkyCompact._LoadedFilesList'][self.variables['i'] - 1]
         == [10, '"0"'])
        :
            self.set_dirty(0)
            if CONDITION:
                self.variables['_blit.backdrop'] = self.lists['SkyCompact._LoadedFilesList'][self.variables['i'] - 1]

                return None

            self.variables['i'] += 4




    async def onbroadcast_Screenflip(self, runtime):
        self.variables['doUpdate'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.set_dirty(0)
        if CONDITION:
            (util.send_event('onbroadcast_' + blitmouse))
            (util.send_event('onbroadcast_' + blitbackground))
            (util.send_event('onbroadcast_' + blitbackSprites))
            (util.send_event('onbroadcast_' + blitbackgroundMask))
            (util.send_event('onbroadcast_' + blitfrontSprites))
            self.set_dirty(0)
            if CONDITION:
                (util.send_event('onbroadcast_' + blitgrid))





    async def onbroadcast_ScreenfnDrawScreen(self, runtime):
        self.variables['scroll'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['palette'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].append(self.variables['scroll'])
        await util.send_event_awaitable('onbroadcast_' + ScreenfnFadeDown)
        await util.send_event_awaitable('onbroadcast_' + ScreenforceRefresh)
        await util.send_event_awaitable('onbroadcast_' + Screenrecreate)
        await util.send_event_awaitable('onbroadcast_' + ScreenspriteEngine)
        self.lists['Params'].append([10, '"false"'])
        await util.send_event_awaitable('onbroadcast_' + Screenflip)
        self.lists['Params'].append(self.variables['palette'])
        self.lists['Params'].append(self.variables['scroll'])
        await util.send_event_awaitable('onbroadcast_' + ScreenfnFadeUp)



    async def onbroadcast_ScreenfnFadeDown(self, runtime):
        self.variables['scroll'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.set_dirty(0)
        if ((not (self.variables['scroll'] == [10, '"123"'])

         and not (self.variables['scroll'] == [10, '"321"'])

        )
         or not ((self.variables['_systemVars.systemFlags'] % (self.variables['SF_NO_SCROLL'] * 4)
        )
         < self.variables['SF_NO_SCROLL'])

        )
        :
            await util.send_event_awaitable('onbroadcast_' + ScratchFaderfadeDown)

        else:
            self.lists['Params'].append([10, '"Screen.fnFadeDown: scroll preparation"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def onbroadcast_ScreenpaletteFadeUpuint8(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + ScratchFaderfadeUp)



    async def onbroadcast_ScreenpaletteFadeUpuint16(self, runtime):
        self.variables['fileNr'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        await util.send_event_awaitable('onbroadcast_' + ScreenpaletteFadeUpuint8)



    async def onbroadcast_ScreenfnFadeUp(self, runtime):
        self.variables['scroll'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['palNum'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.set_dirty(0)
        if CONDITION:
            self.variables['scroll'] = [10, '"0"']

        self.set_dirty(0)
        if (self.variables['scroll'] == [10, '"0"'])
        :
            self.lists['Params'].append([10, '"true"'])
            await util.send_event_awaitable('onbroadcast_' + Screenflip)
            await util.send_event_awaitable('onbroadcast_' + ScratchFaderfadeUp)

        else:
            self.lists['Params'].append([10, '"Screen.fnFadeUp (scrolling left or right)"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def onbroadcast_ScreenwaitForSequence(self, runtime):
        self.lists['Params'].append([10, '"Screen.waitForSequence"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ScreenstartSequence(self, runtime):
        self.variables['_seqInfo.currentSequence'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        await util.send_event_awaitable('onbroadcast_' + scratchgetMillis)
        self.variables['_seqInfo.nextFrame'] = (self.variables['Return value'] + 4)

        self.variables['_seqInfo.currentFrame'] = [10, '"0"']
        ()
        self.variables['_seqInfo.framesLeft'] = self.variables['Return value']
        self.variables['_seqInfo.running'] = [10, '"true"']
        self.variables['_seqInfo.runningItem'] = [10, '"false"']



    async def onbroadcast_ScreenstartSequenceItem(self, runtime):
        self.variables['filenum'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].append([10, '"Screen.startSequenceItem"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)
        await util.send_event_awaitable('onbroadcast_' + scratchgetMillis)
        self.variables['_seqInfo.nextFrame'] = (self.variables['Return value'] + 4)

        self.variables['_seqInfo.currentFrame'] = [10, '"0"']
        ()
        self.variables['_seqInfo.framesLeft'] = self.variables['Return value']
        self.variables['_seqInfo.running'] = [10, '"true"']
        self.variables['_seqInfo.runningItem'] = [10, '"true"']



    async def onbroadcast_ScreenstopSequence(self, runtime):
        self.variables['_seqInfo.running'] = [10, '"false"']
        self.variables['_seqInfo.nextFrame'] = [10, '"0"']
        self.variables['_seqInfo.framesLeft'] = [10, '"0"']



    async def onbroadcast_ScreenprocessSequence(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        await util.send_event_awaitable('onbroadcast_' + scratchgetMillis)
        self.set_dirty(0)
        if CONDITION:
            return None

        self.variables['_seqInfo.nextFrame'] += 4
        ()



    async def onbroadcast_ScreenpaintBox(self, runtime):
        self.lists['Params'].append([10, '"Screen.paintBox"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ScreenshowGrid(self, runtime):
        self.lists['Params'].append([10, '"Screen.showGrid: Shouldn\'t call this as it serves no purpose"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_Scratchinitialise(self, runtime):
        ()



    async def onbroadcast_ScreensequenceRunning(self, runtime):
        self.variables['Return value'] = self.variables['_seqInfo.running']



    async def onbroadcast_deleteScreen(self, runtime):
        self.lists['Params'].append([10, '"delete Screen"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_ScreenseqFramesLeft(self, runtime):
        self.variables['Return value'] = self.variables['_seqInfo.framesLeft']



    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['_seqGrid'] = []
        self.variables['_seqInfo.seqData'] = [10, '""']
        self.set_dirty(0)
        if CONDITION:
            # data_showvariable('_seqInfo.seqData')
            # data_showlist('_seqGrid')
            await self.sleep(5)

        # data_hidevariable('_seqInfo.seqData')
        # data_hidelist('_seqGrid')



    async def onbroadcast_ScreenforceRefresh(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"Screen.forceRefresh - shouldn\'t call this as it serves no purpose!"'])
            await util.send_event_awaitable('onbroadcast_' + scratchwarning)




    async def onbroadcast__blitbackground(self, runtime):
        # pen_clear()
        self.size = (self.variables['Scale'] * 4)

        self.set_dirty(0)
        if CONDITION:
            self.costume = self.get_costume((str(self.variables['_blit.backdrop']) + str([10, '""']))
            )
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append((str((str([10, '"_blitBackground: costume "']) + str(self.variables['_blit.backdrop']))
                ) + str([10, '" not found"']))
                )
                await util.send_event_awaitable('onbroadcast_' + scratchwarning)

            self.xpos = 4
            self.ypos = 4
            # pen_stamp()




    async def onbroadcast__blitgrid(self, runtime):
        ()



    async def onbroadcast__blitbackgroundMask(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['bgMask'] = (str(self.variables['_blit.backdrop']) + str([10, '"_mask"']))

            self.costume = self.get_costume((str(self.variables['bgMask']) + str([10, '""']))
            )
            self.set_dirty(0)
            if CONDITION:
                self.xpos = 4
                self.ypos = 4
                # pen_stamp()

            self.variables['_blit.backdrop'] = [10, '"-1"']





class skysky(SpriteBase):
    async def onbroadcast_SkyEngineinit(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + newDisk)
        self.lists['Params'].append([10, '"255"'])
        await util.send_event_awaitable('onbroadcast_' + newSound)
        await util.send_event_awaitable('onbroadcast_' + DiskdetermineGameVersion)
        self.variables['_SystemVars.gameVersion'] = self.variables['Return value']
        await util.send_event_awaitable('onbroadcast_' + newMusicBase)
        await util.send_event_awaitable('onbroadcast_' + SkyEngineisCDVersion)
        self.set_dirty(0)
        if (self.variables['Return value'] == [10, '"true"'])
        :
            self.variables['_systemVars.systemFlags'] += (self.variables['SF_ALLOW_TEXT'] + self.variables['SF_ALLOW_SPEECH'])


        else:
            self.variables['_systemVars.systemFlags'] += self.variables['SF_ALLOW_TEXT']

        self.variables['_systemVars.systemFlags'] += self.variables['SF_PLAY_VOCS']
        self.variables['_SystemVars.gameSpeed'] = [10, '"80"']
        await util.send_event_awaitable('onbroadcast_' + newSkyCompact)
        await util.send_event_awaitable('onbroadcast_' + newText)
        await util.send_event_awaitable('onbroadcast_' + newMouse)
        await util.send_event_awaitable('onbroadcast_' + newScreen)
        await util.send_event_awaitable('onbroadcast_' + SkyEngineinitItemList)
        await util.send_event_awaitable('onbroadcast_' + SkyEngineloadFixedItems)
        await util.send_event_awaitable('onbroadcast_' + newLogic)
        await util.send_event_awaitable('onbroadcast_' + initialisefader)
        await util.send_event_awaitable('onbroadcast_' + MouseuseLogicInstance)
        await util.send_event_awaitable('onbroadcast_' + newControl)
        await util.send_event_awaitable('onbroadcast_' + LogicuseControlInstance)
        self.variables['_SystemVars.language'] = self.variables['SKY_ENGLISH']



    async def onbroadcast_Scratchinitialise(self, runtime):
        self.variables['TOP_LEFT_Y'] = [10, '"132"']
        self.variables['SKY_ENGLISH'] = [10, '"0"']
        self.variables['SF_FX_OFF'] = round((4
         * 4)

        )

        self.variables['SF_MUS_OFF'] = round((4
         * 4)

        )

        self.variables['SF_CHOOSING'] = round((4
         * 4)

        )

        self.variables['SF_NO_SCROLL'] = round((4
         * 4)

        )

        self.variables['SF_GAME_RESTORED'] = round((4
         * 4)

        )

        self.variables['SF_PLAY_VOCS'] = round((4
         * 4)

        )

        self.variables['SF_ALLOW_SPEECH'] = round((4
         * 4)

        )

        self.variables['SF_ALLOW_TEXT'] = round((4
         * 4)

        )

        self.variables['SF_MOUSE_LOCKED'] = round((4
         * 4)

        )

        self.variables['_SystemVars.gameVersion'] = [10, '"0"']
        self.variables['_SystemVars.mouseFlag'] = [10, '"0"']
        self.variables['_SystemVars.language'] = [10, '"0"']
        self.variables['_SystemVars.currentPalette'] = [10, '"4316"']
        self.variables['_SystemVars.gameSpeed'] = [10, '"0"']
        self.variables['_SystemVars.currentMusic'] = [10, '"0"']
        self.variables['_SystemVars.pastIntro'] = [10, '"false"']
        self.variables['_SystemVars.paused'] = [10, '"false"']
        self.variables['_systemVars.systemFlags'] = [10, '"0"']
        self.variables['keyDown?'] = [10, '"true"']



    async def onbroadcast_SkyEngineisDemo(self, runtime):
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_SkyEngineisCDVersion(self, runtime):
        self.variables['Return value'] = [10, '"false"']



    async def onbroadcast_newSkyEngine(self, runtime):
        self.variables['_fastMode'] = [10, '"false"']



    async def onbroadcast_SkyEnginego(self, runtime):
        self.lists['Params'].append([10, '"1"'])
        self.lists['Params'].append([10, '"SkyEngine.go"'])
        await util.send_event_awaitable('onbroadcast_' + optimisationTimersetNameN)
        self.lists['Params'].append([10, '"2"'])
        self.lists['Params'].append([10, '"Logic.engine"'])
        await util.send_event_awaitable('onbroadcast_' + optimisationTimersetNameN)
        self.lists['Params'].append([10, '"3"'])
        self.lists['Params'].append([10, '"Screen.spriteEngine"'])
        await util.send_event_awaitable('onbroadcast_' + optimisationTimersetNameN)
        self.variables['result'] = [10, '"0"']
        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if :
                self.variables['introSkipped'] = [10, '"false"']
                self.set_dirty(0)
                if CONDITION:
                    await util.send_event_awaitable('onbroadcast_' + newIntro)
                    self.variables['floppyIntro'] = [10, '"false"']
                    self.lists['Params'].append(self.variables['floppyIntro'])
                    await util.send_event_awaitable('onbroadcast_' + IntrodoIntro)
                    self.variables['introSkipped'] = not (self.variables['Return value'] == [10, '"true"'])


                    await util.send_event_awaitable('onbroadcast_' + deleteIntro)


            else:
                self.variables['introSkipped'] = (util.targets['skip?'].variables['costume name']
                 == [10, '"tickbox"'])


            self.lists['Params'].append([10, '"true"'])
            await util.send_event_awaitable('onbroadcast_' + ScreenclearScreen)
            self.set_dirty(0)
            if (self.variables['introSkipped'] == [10, '"true"'])
            :
                await util.send_event_awaitable('onbroadcast_' + ControlrestartGame)
                (util.send_event('onbroadcast_' + ScratchFaderpauseAndFadeUp))

            else:
                await util.send_event_awaitable('onbroadcast_' + LogicinitScreen0)


        await util.send_event_awaitable('onbroadcast_' + scratchgetMillis)
        self.variables['delayCount'] = self.variables['Return value']
        self.set_dirty(0)
        while True:
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append([10, '"1"'])
                await util.send_event_awaitable('onbroadcast_' + optimisationstartTimerN)

            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append([10, '"2"'])
                await util.send_event_awaitable('onbroadcast_' + optimisationstartTimerN)

            await util.send_event_awaitable('onbroadcast_' + SoundcheckFxQueue)
            await util.send_event_awaitable('onbroadcast_' + MousemouseEngine)
            ()
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append([10, '"SkyEngine.go: paused functionality"'])
                await util.send_event_awaitable('onbroadcast_' + scratchwarning)

            await util.send_event_awaitable('onbroadcast_' + Logicengine)
            await util.send_event_awaitable('onbroadcast_' + ScreenprocessSequence)
            await util.send_event_awaitable('onbroadcast_' + Screenrecreate)
            await util.send_event_awaitable('onbroadcast_' + ScreenspriteEngine)
            self.set_dirty(0)
            if (self.variables['Toolbar.run?'] == [10, '"true"'])
            :
                ("0")

            else:
                self.variables['delayCount'] += self.variables['_SystemVars.gameSpeed']
                await util.send_event_awaitable('onbroadcast_' + scratchgetMillis)
                self.variables['needDelay'] = (self.variables['delayCount'] - self.variables['Return value'])

                self.set_dirty(0)
                if CONDITION:
                    self.variables['needDelay'] = [10, '"0"']
                    self.variables['delayCount'] = self.variables['Return value']

                (e)

            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append([10, '"2"'])
                await util.send_event_awaitable('onbroadcast_' + optimisationstopTimerN)

            self.lists['Params'].append([10, '"true"'])
            await util.send_event_awaitable('onbroadcast_' + Screenflip)
            self.set_dirty(0)
            if CONDITION:
                self.lists['Params'].append([10, '"1"'])
                await util.send_event_awaitable('onbroadcast_' + optimisationstopTimerN)

            self.set_dirty(0)
            if CONDITION:
                await util.send_event_awaitable('onbroadcast_' + framecounter)





    async def onbroadcast_SkyEngineinitItemList(self, runtime):
        self.lists['SkyEngine._ItemList'] = []
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['SkyEngine._ItemList'].append([10, '"0"'])




    async def onbroadcast_SkyEngineloadFixedItems(self, runtime):
        self.lists['Params'].append([10, '"36"'])
        await util.send_event_awaitable('onbroadcast_' + diskloadSprite)
        self.lists['SkyEngine._ItemList'][7 - 1] = self.variables['Return value']
        self.variables['i'] = [10, '"49"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['Params'].append(self.variables['i'])
            await util.send_event_awaitable('onbroadcast_' + diskloadSprite)
            self.lists['SkyEngine._ItemList'][(self.variables['i'] + 4)
             - 1] = self.variables['Return value']
            self.variables['i'] += 4

        self.lists['Params'].append([10, '"73"'])
        await util.send_event_awaitable('onbroadcast_' + diskloadSprite)
        self.lists['SkyEngine._ItemList'][7 - 1] = self.variables['Return value']
        self.variables['i'] = [10, '"262"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['Params'].append(self.variables['i'])
            await util.send_event_awaitable('onbroadcast_' + diskloadSprite)
            self.lists['SkyEngine._ItemList'][(self.variables['i'] + 4)
             - 1] = self.variables['Return value']
            self.variables['i'] += 4

        self.lists['Params'].append([10, '"269"'])
        await util.send_event_awaitable('onbroadcast_' + diskloadSprite)
        self.lists['SkyEngine._ItemList'][7 - 1] = self.variables['Return value']
        self.variables['i'] = [10, '"271"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['Params'].append(self.variables['i'])
            await util.send_event_awaitable('onbroadcast_' + diskloadSprite)
            self.lists['SkyEngine._ItemList'][(self.variables['i'] + 4)
             - 1] = self.variables['Return value']
            self.variables['i'] += 4




    async def onbroadcast_SkyEnginefetchItem(self, runtime):
        self.variables['num'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['Return value'] = self.lists['SkyEngine._ItemList'][(self.variables['num'] + 4)
         - 1]




    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['SkyEngine._ItemList'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('SkyEngine._ItemList')
            await self.sleep(5)

        # data_hidelist('SkyEngine._ItemList')




class skysound(SpriteBase):
    async def onbroadcast_newSound(self, runtime):
        self.lists['Sound._SaveSounds'][7 - 1] = [10, '"65535"']
        self.lists['Sound._SaveSounds'][7 - 1] = [10, '"65535"']
        self.variables['_mainSfxVolume'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['_isPaused'] = [10, '"false"']



    async def onbroadcast_SoundplaySounduint16uint16uint8(self, runtime):
        self.variables['channel'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['volume'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['sound'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e, e, e)



    async def onbroadcast_SoundloadSection(self, runtime):
        self.variables['pSection'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        await util.send_event_awaitable('onbroadcast_' + SoundfnStopFx)



    async def onbroadcast_SoundplaySounduint32byteuint32SoundHandle(self, runtime):
        self.lists['Params'].append([10, '"Sound.playSound (uint32, byte*, uint32, SoundHandle*): Shouldn\'t be getting called at all"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_SoundfnStartFx(self, runtime):
        self.variables['channel'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['sound'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Sound._SaveSounds'][(self.variables['channel'] + 4)
         - 1] = [10, '"0"']
        self.variables['screen'] = (self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.SCREEN']
         - 1]
         % 4)

        self.set_dirty(0)
        if CONDITION:
            self.variables['sound'] = [10, '"394"']

        self.set_dirty(0)
        if CONDITION:
            self.variables['sound'] += 4

        self.variables['sfx'] = ((self.variables['sound'] * 4)
         + 4)

        self.variables['roomList'] = (self.variables['sfx'] + 4)

        self.variables['i'] = [10, '"0"']
        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            while not (self.lists['musicList'][(self.variables['roomList'] + self.variables['i'])
             - 1]
             == self.variables['screen'])
            :
                self.variables['i'] += 4
                self.set_dirty(0)
                if CONDITION:
                    return None



        self.variables['volume'] = ((self.lists['musicList'][((self.variables['roomList'] + self.variables['i'])
         + 4)
         - 1]
         * self.variables['_mainSfxVolume'])
         / 4)


        self.set_dirty(0)
        if CONDITION:
            self.lists['_sfxQueue'].append(self.variables['channel'])
            self.lists['_sfxQueue'].append(self.lists['musicList'][self.variables['sfx'] - 1]
            )
            self.lists['_sfxQueue'].append(self.variables['volume'])
            self.lists['_sfxQueue'].append((self.lists['musicList'][(self.variables['sfx'] + 4)
             - 1]
             % 4)
            )
            return None

        self.set_dirty(0)
        if CONDITION:
            self.lists['Sound._SaveSounds'][(self.variables['channel'] + 4)
             - 1] = (self.lists['musicList'][self.variables['sfx'] - 1]
             + (self.variables['volume'] * 4)
            )


        (e, e, e)



    async def onbroadcast_SoundcheckFxQueue(self, runtime):
        self.variables['cnt'] = [10, '"1"']
        self.set_dirty(0)
        while not (self.variables['cnt'] > len(self.lists['_sfxQueue'])
        )
        :
            self.set_dirty(0)
            if CONDITION:
                self.lists['_sfxQueue'][(self.variables['cnt'] + 4)
                 - 1] = (self.lists['_sfxQueue'][(self.variables['cnt'] + 4)
                 - 1]
                 - 4)

                self.set_dirty(0)
                if CONDITION:
                    (e, e, e)
                    self.lists['_sfxQueue'].pop(self.variables['cnt'] - 1)
                    self.lists['_sfxQueue'].pop(self.variables['cnt'] - 1)
                    self.lists['_sfxQueue'].pop(self.variables['cnt'] - 1)
                    self.lists['_sfxQueue'].pop(self.variables['cnt'] - 1)
                    self.variables['cnt'] += 4


            self.variables['cnt'] += 4




    async def onbroadcast_SoundrestoreSfx(self, runtime):
        self.lists['_sfxQueue'] = []
        self.set_dirty(0)
        if CONDITION:
            self.lists['_sfxQueue'].append((self.lists['Sound._SaveSounds'][7 - 1]
             % 4)
            )
            self.lists['_sfxQueue'].append((self.lists['Sound._SaveSounds'][7 - 1]
             / 4)

            )
            self.lists['_sfxQueue'].append([10, '"0"'])
            self.lists['_sfxQueue'].append([10, '"1"'])

        self.set_dirty(0)
        if CONDITION:
            self.lists['_sfxQueue'].append((self.lists['Sound._SaveSounds'][7 - 1]
             % 4)
            )
            self.lists['_sfxQueue'].append((self.lists['Sound._SaveSounds'][7 - 1]
             / 4)

            )
            self.lists['_sfxQueue'].append([10, '"1"'])
            self.lists['_sfxQueue'].append([10, '"1"'])




    async def onbroadcast_SoundfnStopFx(self, runtime):
        self.lists['Sound control'].append([10, '"Stop"'])
        self.lists['Sound control'].append([10, '"0"'])
        self.lists['Sound control'].append([10, '"Stop"'])
        self.lists['Sound control'].append([10, '"1"'])
        self.lists['Sound._SaveSounds'][7 - 1] = [10, '"65535"']
        self.lists['Sound._SaveSounds'][7 - 1] = [10, '"65535"']



    async def onbroadcast_SoundstopSpeech(self, runtime):
        self.lists['Params'].append([10, '"Sound.stopSpeech"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_SoundstartSpeech(self, runtime):
        self.lists['Params'].append([10, '"Sound.startSpeech"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_SoundfnPauseFx(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['_isPaused'] = [10, '"true"']
            self.lists['Sound control'].append([10, '"Pause"'])
            self.lists['Sound control'].append([10, '"0"'])
            self.lists['Sound control'].append([10, '"Pause"'])
            self.lists['Sound control'].append([10, '"1"'])




    async def onbroadcast_SoundfnUnPauseFx(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.variables['_isPaused'] = [10, '"false"']
            self.lists['Sound control'].append([10, '"Unpause"'])
            self.lists['Sound control'].append([10, '"0"'])
            self.lists['Sound control'].append([10, '"Unpause"'])
            self.lists['Sound control'].append([10, '"1"'])




    async def onbroadcast__initialisesound(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + DatagetMusicListData)
        ()



    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['Sound._SaveSounds'] = []
        self.lists['_sfxQueue'] = []
        self.lists['musicList'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('Sound._SaveSounds')
            # data_showlist('_sfxQueue')
            # data_showlist('musicList')
            await self.sleep(5)

        # data_hidelist('Sound._SaveSounds')
        # data_hidelist('_sfxQueue')
        # data_hidelist('musicList')




class skysprites(SpriteBase):
    async def onbroadcast_ScreenspriteEngine(self, runtime):
        self.lists['_blit.backSprites'] = []
        self.lists['_blit.frontSprites'] = []
        self.set_dirty(0)
        if (self.variables['Debug?'] == [10, '"false"'])
        :
            ("0")
            ()
            ("1")

        else:
            self.lists['Params'].append([10, '"doSprites(0)"'])
            await util.send_event_awaitable('onbroadcast_' + scratchgraphicslog)
            ("0")
            self.lists['Params'].append([10, '"sortSprites()"'])
            await util.send_event_awaitable('onbroadcast_' + scratchgraphicslog)
            ()
            self.lists['Params'].append([10, '"doSprites(1)"'])
            await util.send_event_awaitable('onbroadcast_' + scratchgraphicslog)
            ("1")
            self.lists['Params'].append([10, '"end SpriteEngine"'])
            await util.send_event_awaitable('onbroadcast_' + scratchgraphicslog)
            self.lists['Params'].append([10, '""'])
            await util.send_event_awaitable('onbroadcast_' + scratchgraphicslog)




    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['sortList.sprite'] = []
        self.lists['sortList.spriteComp'] = []
        self.lists['sortList.yCood'] = []
        self.lists['_blit.backSprites'] = []
        self.lists['_blit.frontSprites'] = []
        self.lists['Sprites.data'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('sortList.sprite')
            # data_showlist('sortList.spriteComp')
            # data_showlist('sortList.yCood')
            # data_showlist('_blit.backSprites')
            # data_showlist('_blit.frontSprites')
            # data_showlist('Sprites.data')
            await self.sleep(5)

        # data_hidelist('sortList.sprite')
        # data_hidelist('sortList.spriteComp')
        # data_hidelist('sortList.yCood')
        # data_hidelist('_blit.backSprites')
        # data_hidelist('_blit.frontSprites')
        # data_hidelist('Sprites.data')



    async def onbroadcast_Scratchinitialise(self, runtime):
        self.visible = 0
        ()



    async def onbroadcast__blitbackSprites(self, runtime):
        ()



    async def onbroadcast_debug(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Params'].append([10, '"3"'])
            await util.send_event_awaitable('onbroadcast_' + SkyCompactfetchCpt)
            self.lists['Params'].append((str([10, '"costume# "']) + str((self.lists['SkyCompact._RawBuff'][(self.variables['Return value'] + 4)
             - 1]
             / 4)

            ))
            )
            await util.send_event_awaitable('onbroadcast_' + Debugdebug)




    async def onbroadcast__blitfrontSprites(self, runtime):
        ()




class skytext(SpriteBase):
    async def onbroadcast_newText(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.lists['Params'].append([10, '"60150"'])
        await util.send_event_awaitable('onbroadcast_' + DiskloadFile)
        self.variables['_mainCharacterSet.addr'] = self.variables['Return value']
        self.variables['_mainCharacterSet.charHeight'] = [10, '"12"']
        self.variables['_mainCharacterSet.charSpacing'] = [10, '"0"']
        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + TextfnSetFont)
        self.lists['Params'].append([10, '"60520"'])
        await util.send_event_awaitable('onbroadcast_' + DiskloadFile)
        self.variables['_controlCharacterSet.addr'] = self.variables['Return value']
        self.variables['_controlCharacterSet.charHeight'] = [10, '"12"']
        self.variables['_controlCharacterset.charSpacing'] = [10, '"0"']
        self.lists['Params'].append([10, '"60521"'])
        await util.send_event_awaitable('onbroadcast_' + DiskloadFile)
        self.variables['_linkCharacterSet.addr'] = self.variables['Return value']
        self.variables['_linkCharacterSet.charHeight'] = [10, '"12"']
        self.variables['_linkCharacterSet.charSpacing'] = [10, '"1"']



    async def onbroadcast_TextfnSetFont(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.variables['fontNr'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.set_dirty(0)
        if (self.variables['fontNr'] == [10, '"0"'])
        :
            self.variables['_characterSet'] = self.variables['_mainCharacterSet.addr']
            self.variables['_charHeight'] = self.variables['_mainCharacterSet.charHeight']
            self.variables['_dtCharSpacing'] = self.variables['_mainCharacterSet.charSpacing']
            self.variables['textFile'] = [10, '"60150"']

        else:
            self.set_dirty(0)
            if (self.variables['fontNr'] == [10, '"1"'])
            :
                self.variables['_characterSet'] = self.variables['_linkCharacterSet.addr']
                self.variables['_charHeight'] = self.variables['_linkCharacterSet.charHeight']
                self.variables['_dtCharSpacing'] = self.variables['_linkCharacterSet.charSpacing']
                self.variables['textFile'] = [10, '"60521"']

            else:
                self.variables['_characterSet'] = self.variables['_controlCharacterSet.addr']
                self.variables['_charHeight'] = self.variables['_controlCharacterSet.charHeight']
                self.variables['_dtCharSpacing'] = self.variables['_controlCharacterset.charSpacing']
                self.variables['textFile'] = [10, '"60520"']


        self.variables['_curCharSet'] = self.variables['fontNr']



    async def onbroadcast_TextfnTextModule(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.variables['textNo'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['textInfoId'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].append([10, '"1"'])
        await util.send_event_awaitable('onbroadcast_' + TextfnSetFont)
        self.lists['Params'].append(self.variables['textInfoId'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactfetchCpt)
        self.variables['msgData'] = self.variables['Return value']
        (e, e, e, "209", "false")
        self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.RESULT']
         - 1] = self.variables['textId.compactNum']
        self.lists['Params'].append(self.variables['textId.compactNum'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactfetchCpt)
        self.variables['textCompact'] = self.variables['Return value']
        self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
         - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['msgData'] + 4)
         - 1]

        self.lists['SkyCompact._RawBuff'][(self.variables['textCompact'] + 4)
         - 1] = self.lists['SkyCompact._RawBuff'][(self.variables['msgData'] + 4)
         - 1]

        self.lists['Params'].append([10, '"0"'])
        await util.send_event_awaitable('onbroadcast_' + TextfnSetFont)



    async def onbroadcast_TextfnPointerText(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.variables['mouseY'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['mouseX'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['pointedId'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].append(self.variables['pointedId'])
        await util.send_event_awaitable('onbroadcast_' + SkyCompactfetchCpt)
        self.variables['ptrComp'] = self.variables['Return value']
        (e, "128", "8", "242", "false")
        self.variables['text'] = self.variables['Return value']
        self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.CURSOR_ID']
         - 1] = self.lists['displayedText.compactNum'][self.variables['Return value'] - 1]

        self.set_dirty(0)
        if not (self.lists['Logic._ScriptVariables'][util.targets['sky.logic'].variables['scriptVariableOffsets.MENU']
         - 1]
         == [10, '"0"'])

        :
            self.variables['mouseOfsY'] = (self.variables['TOP_LEFT_Y'] - 4)

            self.set_dirty(0)
            if (self.variables['mouseX'] < [10, '"150"'])
            :
                self.variables['mouseOfsX'] = [10, '"10"']

            else:
                self.variables['mouseOfsX'] = (4 - self.lists['displayedText.textWidth'][self.variables['Return value'] - 1]
                )



        else:
            self.variables['mouseOfsY'] = (self.variables['TOP_LEFT_Y'] - 4)

            self.set_dirty(0)
            if (self.variables['mouseX'] < [10, '"150"'])
            :
                self.variables['mouseOfsX'] = [10, '"5"']

            else:
                self.variables['mouseOfsX'] = (4 - self.lists['displayedText.textWidth'][self.variables['Return value'] - 1]
                )



        self.lists['Params'].append((self.variables['mouseX'] + self.variables['mouseOfsX'])
        )
        self.set_dirty(0)
        if ((self.variables['mouseY'] + self.variables['mouseOfsY'])
         < self.variables['TOP_LEFT_Y'])
        :
            self.lists['Params'].append((self.variables['TOP_LEFT_Y'] - 4)
            )

        else:
            self.lists['Params'].append(((self.variables['mouseY'] + self.variables['mouseOfsY'])
             - 4)
            )

        self.variables['_pointerTextId'] = self.variables['Return value']
        self.lists['Params'].append(self.variables['Return value'])
        await util.send_event_awaitable('onbroadcast_' + blittext)



    async def onbroadcast_TextlogicCursor(self, runtime):
        ("This needs access to the sprite ids as it's used for sliding text around while pointing at things (for example)")
        self.set_dirty(0)
        if CONDITION:
            return None

        self.variables['mouseY'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['mouseX'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['textCompact'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].append([10, '"Text.logicCursor"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_TextdisplayTextuint32uint8booluint16uint8(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.variables['color'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['pixelWidth'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['center'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['textNum'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e)
        (e, e, e)



    async def onbroadcast_TextdisplayTextcharuint8booluint16uint8(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.variables['color'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['pixelWidth'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['center'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['textPtr'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e, e, e)



    async def onbroadcast_TextchangeTextSpriteColor(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            await util.send_event_awaitable('onbroadcast_' + TextchangeTextSpriteColor_internal)
            self.lists['Params'].pop(len(self.lists['Params'])
             - 1)
            self.lists['Params'].pop(len(self.lists['Params'])
             - 1)




    async def onbroadcast_TextgiveCurrentCharSet(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.lists['Params'].append([10, '"Text.giveCurrentCharSet"'])
        await util.send_event_awaitable('onbroadcast_' + scratchwarning)



    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['_textBuffer'] = []
        self.lists['_huffTree.lChild'] = []
        self.lists['_huffTree.rChild'] = []
        self.lists['_huffTree.value'] = []
        self.lists['centerTable'] = []
        self.lists['_textIdSlot'] = []
        self.lists['displayedText.compactNum'] = []
        self.lists['displayedText.textData'] = []
        self.lists['displayedText.textWidth'] = []
        self.lists['_dest'] = []
        self.lists['displayText.textDataLength'] = []
        self.lists['bufferedBlit'] = []
        self.lists['Text._BufferedDestroy'] = []
        self.visible = 0
        # control_delete_this_clone()



    async def onbroadcast_Scratchinitialise(self, runtime):
        self.variables['clone?'] = [10, '"false"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['_textBuffer'].append([10, '"0"'])

        self.set_dirty(0)
        for _ in range(TIMES):
            self.lists['centerTable'].append([10, '"0"'])

        await util.send_event_awaitable('onbroadcast_' + DatagetHuffData)
        self.variables['hex'] = self.variables['Return value']
        self.variables['i'] = [10, '"0"']
        self.set_dirty(0)
        for _ in range(TIMES):
            (e, e)
            self.variables['i'] += 4
            self.lists['_huffTree.lChild'].append(self.variables['Return value'])
            (e, e)
            self.variables['i'] += 4
            self.lists['_huffTree.rChild'].append(self.variables['Return value'])
            (e, e)
            self.variables['i'] += 4
            self.lists['_huffTree.value'].append(self.variables['Return value'])

        self.variables['hex'] = [10, '""']
        self.variables['_pointerTextId'] = [10, '"0"']



    async def onbroadcast__blittext(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.lists['bufferedBlit'].append(self.lists['_textIdSlot'][self.lists['Params'][len(self.lists['Params'])
         - 1]
         - 1]
        )
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['bufferedBlit'].append(self.lists['Params'][len(self.lists['Params'])
         - 1]
        )
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['bufferedBlit'].append(self.lists['Params'][len(self.lists['Params'])
         - 1]
        )
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        ()



    async def onbroadcast_TextlowTextManager(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.variables['center'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['color'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['logicNum'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['width'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['textNum'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        (e, e, e, e, e)



    async def onbroadcast__blitdestroyText(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Text._BufferedDestroy'].append(self.lists['Params'][len(self.lists['Params'])
             - 1]
            )
            self.lists['Params'].pop(len(self.lists['Params'])
             - 1)
            await util.send_event_awaitable('onbroadcast_' + blitDestroyText_internal)
            ()




    async def clone_start(self, runtime):
        self.variables['clone?'] = [10, '"true"']
        self.visible = 1



    async def onbroadcast__blitDestroyText_internal(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                # control_delete_this_clone()





    async def onbroadcast_TextgetCompactNumFromId(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.variables['i'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['Return value'] = self.lists['displayedText.compactNum'][self.variables['i'] - 1]




    async def onbroadcast_TextchangeTextSpriteColor_internal(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                self.set_effect('COLOR', self.lists['textColours'][((self.lists['Params'][len(self.lists['Params'])
                 - 1]
                 % len(self.lists['textColours'])
                )
                 + 4)
                 - 1]
                )





    async def onbroadcast__blitprepText(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        self.lists['bufferedBlit'].append(self.lists['_textIdSlot'][self.lists['Params'][len(self.lists['Params'])
         - 1]
         - 1]
        )
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['bufferedBlit'].append(self.lists['Params'][len(self.lists['Params'])
         - 1]
        )
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['bufferedBlit'].append(self.lists['Params'][len(self.lists['Params'])
         - 1]
        )
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)



    async def onbroadcast__blitbufferedText(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            return None

        ()



    async def onbroadcast__blitprepBufferedDestroy(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Text._BufferedDestroy'].append(self.lists['Params'][len(self.lists['Params'])
             - 1]
            )
            self.lists['Params'].pop(len(self.lists['Params'])
             - 1)




    async def onbroadcast__blitbufferedDestroy(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            await util.send_event_awaitable('onbroadcast_' + blitDestroyText_internal)
            ()





class scratchmain(SpriteBase):
    async def green_flag(self, runtime):
        self.variables['Debug?'] = [10, '"false"']
        # pen_clear()
        self.costume = self.get_costume('thumbnail2')
        self.visible = 1
        self.variables['Scale'] = [10, '"1.5"']
        await util.send_event_awaitable('onbroadcast_' + changescale)
        await util.send_event_awaitable('onbroadcast_' + Scratchreset)
        self.variables['start clock'] = (time.time() / 86400 - 10957)

        await util.send_event_awaitable('onbroadcast_' + initialisedebug)
        await util.send_event_awaitable('onbroadcast_' + Scratchinitialise)
        await util.send_event_awaitable('onbroadcast_' + initialisesound)
        await util.send_event_awaitable('onbroadcast_' + newSkyEngine)
        await util.send_event_awaitable('onbroadcast_' + SkyEngineinit)
        self.visible = 0
        await util.send_event_awaitable('onbroadcast_' + SkyEnginego)



    async def onbroadcast_scratchgetMillis(self, runtime):
        self.variables['Return value'] = round((((time.time() / 86400 - 10957)
         - self.variables['start clock'])
         * 4)
        )




    async def onbroadcast_Scratchthumbnail(self, runtime):
        self.variables['doing thumbnail?'] = [10, '"true"']
        await util.send_event_awaitable('onbroadcast_' + Scratchreset)
        self.costume = self.get_costume('thumbnail')
        self.xpos = 4
        self.ypos = 4
        # looks_gotofrontback()
        self.visible = 1
        # pen_clear()
        self.variables['doing thumbnail?'] = [10, '"false"']



    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['Generic list'] = []
        self.lists['Params'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('Generic list')
            # data_showlist('Params')
            await self.sleep(5)

        # data_hidelist('Generic list')
        # data_hidelist('Params')



    async def onbroadcast_BitwiseOru16(self, runtime):
        self.variables['num1'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['num2'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['Return value'] = [10, '"0"']
        self.variables['addVal'] = [10, '"1"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.set_dirty(0)
            if CONDITION:
                self.variables['Return value'] += self.variables['addVal']

            self.variables['num1'] = (self.variables['num1'] / 4)


            self.variables['num2'] = (self.variables['num2'] / 4)


            self.variables['addVal'] += self.variables['addVal']




    async def onbroadcast_BitwiseXORu16(self, runtime):
        self.variables['num1'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['num2'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['Return value'] = [10, '"0"']
        self.variables['addVal'] = [10, '"1"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.set_dirty(0)
            if CONDITION:
                self.variables['Return value'] += self.variables['addVal']

            self.variables['num1'] = (self.variables['num1'] / 4)


            self.variables['num2'] = (self.variables['num2'] / 4)


            self.variables['addVal'] += self.variables['addVal']




    async def onbroadcast_BitwiseAndu16(self, runtime):
        self.variables['num1'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['num2'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['Return value'] = [10, '"0"']
        self.variables['addVal'] = [10, '"1"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.set_dirty(0)
            if CONDITION:
                self.variables['Return value'] += self.variables['addVal']

            self.variables['num1'] = (self.variables['num1'] / 4)


            self.variables['num2'] = (self.variables['num2'] / 4)


            self.variables['addVal'] += self.variables['addVal']




    async def onbroadcast_SkyEnginedeinitVirgin(self, runtime):
        self.visible = 0




class scratchfader(SpriteBase):
    async def onbroadcast__initialisefader(self, runtime):
        await util.send_event_awaitable('onbroadcast_' + SkyEnginedeinitVirgin)
        self.variables['clone?'] = [10, '"false"']
        self.variables['alpha'] = [10, '"0"']
        self.xpos = 4
        self.ypos = 4
        self.costume = self.get_costume('white')
        self.set_effect('GHOST', self.variables['alpha'])
        self.set_effect('BRIGHTNESS', 4)
        self.visible = 1
        # looks_gotofrontback()
        await util.send_event_awaitable('onbroadcast_' + initialisetoolbar)



    async def onbroadcast_ScratchFaderfadeUp(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            while not (self.variables['alpha'] == [10, '"100"'])
            :
                self.variables['alpha'] += 4
                self.set_effect('GHOST', self.variables['alpha'])





    async def onbroadcast_ScratchFaderfadeDown(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            while not (self.variables['alpha'] == [10, '"0"'])
            :
                self.variables['alpha'] += 4
                self.set_effect('GHOST', self.variables['alpha'])





    async def clone_start(self, runtime):
        self.variables['clone?'] = [10, '"true"']
        self.clear_effects()
        self.costume = self.get_costume('border')



    async def onbroadcast_changescale(self, runtime):
        self.size = (self.variables['Scale'] * 4)




    async def onbroadcast_Scratchinitialise(self, runtime):
        self.visible = 0



    async def onbroadcast_ScratchFaderpauseAndFadeUp(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            await self.sleep(5)
            await util.send_event_awaitable('onbroadcast_' + ScratchFaderfadeUp)




    async def onbroadcast_Scratchreset(self, runtime):
        self.visible = 0




class scratchsfx(SpriteBase):
    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['Sound control'] = []
        self.lists['sounds'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('Sound control')
            # data_showlist('sounds')
            await self.sleep(5)

        # data_hidelist('Sound control')
        # data_hidelist('sounds')



    async def onbroadcast_Scratchinitialise(self, runtime):
        self.variables['clone?'] = [10, '"false"']
        self.lists['sounds'].append([10, '"s0-fx1-l"'])
        self.lists['sounds'].append([10, '"s0-fx2"'])
        self.lists['sounds'].append([10, '"s1-fx3"'])
        self.lists['sounds'].append([10, '"s1-fx4"'])
        self.lists['sounds'].append([10, '"s1-fx4-l"'])
        self.lists['sounds'].append([10, '"s1-fx5"'])
        self.lists['sounds'].append([10, '"s1-fx6"'])
        self.lists['sounds'].append([10, '"s1-fx7"'])
        self.lists['sounds'].append([10, '"s1-fx7-l"'])
        self.lists['sounds'].append([10, '"s1-fx8-l"'])
        self.lists['sounds'].append([10, '"s1-fx9"'])
        self.lists['sounds'].append([10, '"s1-fx10"'])
        self.lists['sounds'].append([10, '"s1-fx11"'])
        self.lists['sounds'].append([10, '"s1-fx11-l"'])
        self.lists['sounds'].append([10, '"s1-fx12"'])
        self.lists['sounds'].append([10, '"s1-fx13"'])
        self.lists['sounds'].append([10, '"s1-fx14"'])
        self.lists['sounds'].append([10, '"s1-fx17-l"'])
        self.lists['sounds'].append([10, '"s1-fx18"'])
        self.lists['sounds'].append([10, '"s1-fx19"'])
        self.lists['sounds'].append([10, '"s1-fx26"'])
        self.variables['isPlaying?'] = [10, '"false"']
        self.variables['channel'] = [10, '"0"']
        # control_create_clone_of('_myself_')
        self.variables['channel'] = [10, '"1"']
        # control_create_clone_of('_myself_')



    async def clone_start(self, runtime):
        self.variables['clone?'] = [10, '"true"']
        self.set_dirty(0)
        while True:
            self.set_dirty(0)
            while not (len(self.lists['Sound control'])
             == [10, '"0"'])
            :
                self.variables['command'] = self.lists['Sound control'][7 - 1]

                self.set_dirty(0)
                if (self.variables['command'] == [10, '"Play"'])
                :
                    self.set_dirty(0)
                    if CONDITION:
                        self.set_dirty(0)
                        if CONDITION:
                            self.variables['isPlaying?'] = [10, '"false"']
                            # control_create_clone_of('_myself_')
                            # control_delete_this_clone()



                else:
                    self.set_dirty(0)
                    if (self.variables['command'] == [10, '"Stop"'])
                    :
                        self.set_dirty(0)
                        if CONDITION:
                            self.lists['Sound control'].pop(7 - 1)
                            self.lists['Sound control'].pop(7 - 1)
                            self.set_dirty(0)
                            if CONDITION:
                                self.variables['isPlaying?'] = [10, '"false"']
                                # control_create_clone_of('_myself_')
                                # control_delete_this_clone()



                    else:
                        self.set_dirty(0)
                        if (self.variables['command'] == [10, '"Pause"'])
                        :
                            self.set_dirty(0)
                            if CONDITION:
                                self.lists['Sound control'].pop(7 - 1)
                                self.lists['Sound control'].pop(7 - 1)
                                # sound_setvolumeto(4)


                        else:
                            self.set_dirty(0)
                            if (self.variables['command'] == [10, '"Unpause"'])
                            :
                                self.set_dirty(0)
                                if CONDITION:
                                    self.lists['Sound control'].pop(7 - 1)
                                    self.lists['Sound control'].pop(7 - 1)
                                    # sound_setvolumeto((self.variables['volume'] * ((self.variables['_systemVars.systemFlags'] % (self.variables['SF_FX_OFF'] * 4)
                                    )
                                     < self.variables['SF_FX_OFF'])
                                    )
                                    )


                            else:









    async def clone_start(self, runtime):
        self.set_dirty(0)
        while True:
            self.set_dirty(0)
            while not (len(self.lists['Sound control'])
             == [10, '"0"'])
            :
                self.variables['command'] = self.lists['Sound control'][7 - 1]

                self.set_dirty(0)
                if (self.variables['command'] == [10, '"Play"'])
                :
                    self.set_dirty(0)
                    if CONDITION:
                        self.set_dirty(0)
                        if CONDITION:
                            self.variables['volume'] = ((self.lists['Sound control'][7 - 1]
                             * 4)
                             / 4)

                            self.variables['name'] = self.lists['Sound control'][7 - 1]

                            self.set_dirty(0)
                            if CONDITION:
                                self.set_dirty(0)
                                if CONDITION:
                                    self.lists['Params'].append((str([10, '"Missing sfx: "']) + str(self.variables['name']))
                                    )
                                    await util.send_event_awaitable('onbroadcast_' + scratchwarning)


                            self.variables['isPlaying?'] = [10, '"true"']
                            self.lists['Sound control'].pop(7 - 1)
                            self.lists['Sound control'].pop(7 - 1)
                            self.lists['Sound control'].pop(7 - 1)
                            self.lists['Sound control'].pop(7 - 1)
                            # sound_setvolumeto((self.variables['volume'] * ((self.variables['_systemVars.systemFlags'] % (self.variables['SF_FX_OFF'] * 4)
                            )
                             < self.variables['SF_FX_OFF'])
                            )
                            )
                            self.set_dirty(0)
                            if CONDITION:
                                # sound_playuntildone(self.variables['name'])

                            self.set_dirty(0)
                            if CONDITION:
                                self.set_dirty(0)
                                while True:
                                    # sound_playuntildone((str(self.variables['name']) + str([10, '"-l"']))
                                    )


                            self.variables['isPlaying?'] = [10, '"false"']



                else:






    async def onbroadcast_FxsetEnabled(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            # sound_setvolumeto((self.variables['volume'] * ((self.variables['_systemVars.systemFlags'] % (self.variables['SF_FX_OFF'] * 4)
            )
             < self.variables['SF_FX_OFF'])
            )
            )





class data(SpriteBase):
    async def onbroadcast_DatagetCompactDataFile(self, runtime):
        self.variables['Return value'] = self.variables['compactDataFile']



    async def onbroadcast_DataconvertGenericU16ListToReturnValue(self, runtime):
        self.variables['Return value'] = [10, '""']
        self.variables['i'] = [10, '"1"']
        self.set_dirty(0)
        for _ in range(TIMES):
            self.variables['u16'] = self.lists['Generic list'][self.variables['i'] - 1]

            self.variables['byte'] = (self.variables['u16'] % 4)

            self.variables['Return value'] = (str(self.variables['Return value']) + str(self.lists['Hex'][((self.variables['byte'] / 4)

             + 4)
             - 1]
            ))

            self.variables['Return value'] = (str(self.variables['Return value']) + str(self.lists['Hex'][((self.variables['byte'] % 4)
             + 4)
             - 1]
            ))

            self.variables['byte'] = (self.variables['u16'] / 4)


            self.variables['Return value'] = (str(self.variables['Return value']) + str(self.lists['Hex'][((self.variables['byte'] / 4)

             + 4)
             - 1]
            ))

            self.variables['Return value'] = (str(self.variables['Return value']) + str(self.lists['Hex'][((self.variables['byte'] % 4)
             + 4)
             - 1]
            ))

            self.variables['i'] += 4

        self.lists['Generic list'] = []



    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['fileData'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('fileData')
            await self.sleep(5)

        # data_hidelist('fileData')



    async def onbroadcast_Scratchinitialise(self, runtime):
        ()



    async def onbroadcast_DataloadFile(self, runtime):
        self.variables['i'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['Return value'] = self.lists['fileData'][self.variables['i'] - 1]




    async def onbroadcast_DatagetScriptVariables(self, runtime):
        self.variables['Return value'] = self.variables['scriptVariables']



    async def onbroadcast_DatagetCompactOffsets(self, runtime):
        self.variables['Return value'] = self.variables['compactOffsets']



    async def onbroadcast_DatagetMegaSetOffsets(self, runtime):
        self.variables['Return value'] = self.variables['megaSetOffsets']



    async def onbroadcast_DatagetTurnTableOffsets(self, runtime):
        self.variables['Return value'] = self.variables['turnTableOffsets']



    async def onbroadcast_DatagetGameGrids(self, runtime):
        self.variables['Return value'] = self.variables['gameGrids']



    async def onbroadcast_DatagetGridConvertTable(self, runtime):
        self.variables['Return value'] = self.variables['gridConvertTable']



    async def onbroadcast_DatagetHuffData(self, runtime):
        self.variables['Return value'] = self.variables['huffData']



    async def onbroadcast_DatagetMusicListData(self, runtime):
        self.variables['Return value'] = self.variables['musicListData']




class debug(SpriteBase):
    async def onbroadcast_scratchwarning(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Warnings'].append(self.lists['Params'][len(self.lists['Params'])
             - 1]
            )

        await util.send_event_awaitable('onbroadcast_' + Debugdebug)



    async def onbroadcast_scratcherror(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Errors'].append(self.lists['Params'][len(self.lists['Params'])
             - 1]
            )

        await util.send_event_awaitable('onbroadcast_' + Debugdebug)



    async def onbroadcast_Scratchreset(self, runtime):
        self.lists['Warnings'] = []
        self.lists['Errors'] = []
        self.lists['Debug log'] = []
        self.lists['Sprite files'] = []
        self.lists['Graphics log'] = []
        self.lists['fps'] = []
        self.lists['allOptimisationTimers'] = []
        self.lists['Debug.optimisationTimer'] = []
        self.lists['optimisationTimerName'] = []
        self.lists['Debug.timers'] = []
        self.set_dirty(0)
        if CONDITION:
            # data_showlist('Warnings')
            # data_showlist('Errors')
            # data_showlist('Debug log')
            # data_showlist('Sprite files')
            # data_showlist('Graphics log')
            # data_showlist('fps')
            # data_showlist('allOptimisationTimers')
            # data_showlist('Debug.optimisationTimer')
            # data_showlist('optimisationTimerName')
            # data_showlist('Debug.timers')
            await self.sleep(5)

        # data_hidelist('Warnings')
        # data_hidelist('Errors')
        # data_hidelist('Debug log')
        # data_hidelist('Sprite files')
        # data_hidelist('Graphics log')
        # data_hidelist('fps')
        # data_hidelist('allOptimisationTimers')
        # data_hidelist('Debug.optimisationTimer')
        # data_hidelist('optimisationTimerName')
        # data_hidelist('Debug.timers')
        # data_hidevariable('FPS')



    async def onbroadcast_Debuglogic(self, runtime):
        self.variables['logic'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Debug log'].append((str([10, '"LOGIC: "']) + str(self.lists['logic_table_names'][(self.variables['logic'] + 4)
         - 1]
        ))
        )



    async def onbroadcast_Debugscript(self, runtime):
        self.lists['Generic list'] = []
        self.lists['Generic list'].append(self.lists['Params'][(len(self.lists['Params'])
         - 4)
         - 1]
        )
        self.lists['Generic list'].append(self.lists['Params'][(len(self.lists['Params'])
         - 4)
         - 1]
        )
        self.lists['Generic list'].append(self.lists['Params'][len(self.lists['Params'])
         - 1]
        )
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['command'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Debug log'].append((str([10, '"SCRIPT: "']) + str(self.lists['opcodes'][(self.variables['command'] + 4)
         - 1]
        ))
        )
        self.set_dirty(0)
        if ((self.variables['command'] == [10, '"0"'])
         or (self.variables['command'] == [10, '"6"'])
        )
        :
            self.lists['Debug log'].append((str([10, '" "']) + str(self.lists['scriptVars'][((self.lists['Generic list'][7 - 1]
             / 4)
             + 4)
             - 1]
            ))
            )

        else:
            self.variables['i'] = [10, '"1"']
            self.set_dirty(0)
            for _ in range(TIMES):
                self.lists['Debug log'].append((str([10, '" "']) + str(self.lists['Generic list'][self.variables['i'] - 1]
                ))
                )
                self.variables['i'] += 4


        self.lists['Debug log'].append([10, '""'])



    async def onbroadcast_Debugmcode(self, runtime):
        self.variables['c'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['b'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['a'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['mcode'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Debug log'].append((str((str((str((str((str((str((str((str([10, '"MCODE: "']) + str(self.lists['mcodes'][(self.variables['mcode'] + 4)
         - 1]
        ))
        ) + str([10, '"("']))
        ) + str(self.variables['a']))
        ) + str([10, '", "']))
        ) + str(self.variables['b']))
        ) + str([10, '", "']))
        ) + str(self.variables['c']))
        ) + str([10, '")"']))
        )



    async def onbroadcast_Debugdebug(self, runtime):
        self.variables['string'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Debug log'].append(self.variables['string'])



    async def onbroadcast_DebugspriteFiles(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.lists['Sprite files'].append(self.lists['Params'][len(self.lists['Params'])
             - 1]
            )

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)



    async def onbroadcast_scratchgraphicslog(self, runtime):
        self.lists['Graphics log'].append(self.lists['Params'][len(self.lists['Params'])
         - 1]
        )
        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)



    async def onbroadcast__framecounter(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            ()

        self.set_dirty(0)
        if CONDITION:
            self.set_dirty(0)
            if CONDITION:
                ()





    async def onbroadcast__initialisedebug(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            await util.send_event_awaitable('onbroadcast_' + optimisationinitialise)

        self.variables['Debug.Fps?'] = [10, '"false"']
        self.variables['Debug.Timers?'] = [10, '"false"']
        self.variables['Debug.Grid?'] = [10, '"false"']



    async def onbroadcast__optimisationstartTimerN(self, runtime):
        self.variables['i'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Debug.optimisationTimer'][(self.variables['i'] * 4)
         - 1] = (time.time() / 86400 - 10957)




    async def onbroadcast__optimisationstopTimerN(self, runtime):
        self.variables['i'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['Debug.optimisationTimer'][((self.variables['i'] * 4)
         - 4)
         - 1] = (self.lists['Debug.optimisationTimer'][((self.variables['i'] * 4)
         - 4)
         - 1]
         + ((time.time() / 86400 - 10957)
         - self.lists['Debug.optimisationTimer'][(self.variables['i'] * 4)
         - 1]
        )
        )




    async def onbroadcast__optimisationTimersetNameN(self, runtime):
        self.variables['name'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.variables['i'] = self.lists['Params'][len(self.lists['Params'])
         - 1]

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        self.lists['optimisationTimerName'][self.variables['i'] - 1] = self.variables['name']



    async def onbroadcast__optimisationinitialise(self, runtime):
        ()




class logo(SpriteBase):
    async def onbroadcast_SkyEngineinitVirgin(self, runtime):
        self.costume = self.get_costume('logo')
        self.xpos = 4
        self.ypos = 4
        self.set_effect('GHOST', 4)
        # looks_gotofrontback()
        # looks_goforwardbackwardlayers(7)
        self.visible = 1
        # control_create_clone_of('_myself_')
        self.set_dirty(0)
        for _ in range(TIMES):
            self.change_effect('GHOST', 4)
            await self.sleep(5)




    async def onbroadcast_Scratchinitialise(self, runtime):
        self.visible = 0
        self.variables['clone?'] = [10, '"false"']
        # control_delete_this_clone()



    async def onbroadcast_SkyEnginedeinitVirgin(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            # looks_gotofrontback()
            self.set_dirty(0)
            for _ in range(TIMES):
                self.change_effect('GHOST', 4)

            await util.send_event_awaitable('onbroadcast_' + hidelogo)
            # pen_clear()
            # control_delete_this_clone()




    async def clone_start(self, runtime):
        self.variables['clone?'] = [10, '"true"']
        self.costume = self.get_costume('black')



    async def onbroadcast_hidelogo(self, runtime):
        self.set_dirty(0)
        if CONDITION:
            self.visible = 0





class skip(SpriteBase):
    async def onbroadcast_Scratchinitialise(self, runtime):
        # looks_gotofrontback()
        self.xpos = 4
        self.ypos = 4
        self.visible = 1
        self.costume = self.get_costume('crossbox')



    async def onbroadcast_hidelogo(self, runtime):
        self.visible = 0



    async def onbroadcast_Scratchreset(self, runtime):
        self.visible = 0




class toolbar(SpriteBase):
    async def onbroadcast__initialisetoolbar(self, runtime):
        # looks_gotofrontback()
        self.visible = 1
        self.ypos = Y
        self.xpos = X
        self.variables['state?'] = [10, '"false"']
        self.variables['cloneId'] = [10, '"use"']
        # control_create_clone_of('_myself_')
        self.xpos = X
        self.costume = self.get_costume('load')
        self.variables['state?'] = [10, '"false"']
        self.variables['cloneId'] = [10, '"load"']
        # control_create_clone_of('_myself_')
        self.xpos = X
        self.costume = self.get_costume('save')
        self.variables['state?'] = [10, '"false"']
        self.variables['cloneId'] = [10, '"save"']
        # control_create_clone_of('_myself_')
        self.xpos = X
        self.variables['state?'] = [10, '"true"']
        self.variables['cloneId'] = [10, '"sound"']
        # control_create_clone_of('_myself_')
        self.xpos = X
        self.variables['state?'] = [10, '"true"']
        self.variables['cloneId'] = [10, '"music"']
        # control_create_clone_of('_myself_')
        self.xpos = X
        self.variables['state?'] = [10, '"false"']
        self.variables['cloneId'] = [10, '"run"']
        # control_create_clone_of('_myself_')
        self.xpos = X
        self.costume = self.get_costume('help')
        self.variables['state?'] = [10, '"false"']
        self.variables['cloneId'] = [10, '"help"']
        # control_create_clone_of('_myself_')
        self.variables['cloneId'] = [10, '"master"']
        self.visible = 0
        await util.send_event_awaitable('onbroadcast_' + ToolbarupdateToolbar)



    async def onbroadcast_Scratchreset(self, runtime):
        self.visible = 0
        # control_delete_this_clone()



    async def onbroadcast_ToolbarupdateToolbar(self, runtime):
        ()



    async def clone_start(self, runtime):
        self.variables['newState?'] = self.variables['state?']
        self.variables['state?'] = not (self.variables['state?'] == [10, '"true"'])






class info(SpriteBase):
    async def onbroadcast_Infoshow(self, runtime):
        self.variables['clone?'] = [10, '"false"']
        self.xpos = 4
        self.ypos = 4
        self.costume = self.get_costume('forward')
        self.visible = 1
        self.variables['Info.Page'] = [10, '"1"']
        # control_create_clone_of('_myself_')
        while not (self.variables['Info.Page'] > [10, '"6"'])
        :
            await self._yield()
        self.visible = 0



    async def clone_start(self, runtime):
        self.variables['clone?'] = [10, '"true"']
        self.xpos = 4
        self.ypos = 4
        self.costume = self.get_costume('page 1')
        self.variables['page'] = [10, '"1"']
        self.set_dirty(0)
        while not (self.variables['Info.Page'] > [10, '"6"'])
        :
            while not (self.variables['Info.Page'] > self.variables['page'])
            :
                await self._yield()
            next_costume = self.costume['number'] + 1
            if next_costume == len(self.costumes):
                self.costume = self.costumes[0]
            else:
                self.costume = self.costumes[next_costume]
            self.variables['page'] = self.variables['Info.Page']

        # control_delete_this_clone()



    async def onbroadcast_Scratchreset(self, runtime):
        self.visible = 0
        # control_delete_this_clone()




class textbackground(SpriteBase):
    async def onbroadcast__textstippleBackground(self, runtime):
        self.size = (self.variables['Scale'] * 4)

        self.xpos = 4
        self.ypos = (4 + ((4 - (self.lists['Params'][len(self.lists['Params'])
         - 1]
         * 4)
        )
         * self.variables['Scale'])
        )

        self.size = (self.variables['Scale'] * 4)

        self.lists['Params'].pop(len(self.lists['Params'])
         - 1)
        # looks_gotofrontback()
        self.visible = 1



    async def onbroadcast_Scratchreset(self, runtime):
        self.visible = 0



    async def onbroadcast__texthideBackground(self, runtime):
        self.visible = 0




class notes(SpriteBase):
    pass

